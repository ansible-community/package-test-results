#!/usr/bin/env python3

# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: GPL-3.0-or-later
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import dataclasses
import webbrowser
from collections import Counter, defaultdict
from collections.abc import Iterable
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict, cast

import jinja2
import pyperclip  # type: ignore[import]
import typer
from antsibull.types import CollectionName, make_collection_mapping
from antsibull_core.yaml import load_yaml_file
from yarl import URL

if TYPE_CHECKING:
    from antsibull.from_source.verify import FileError, FileErrorOutput
    from antsibull.sanity_tests import Output as SanityTestsOutput
    from antsibull.tagging import CollectionTagData

app = typer.Typer()
env = jinja2.Environment(
    autoescape=jinja2.select_autoescape(default_for_string=False),
    trim_blocks=True,
    undefined=jinja2.StrictUndefined,
    loader=jinja2.FileSystemLoader(Path(__file__).resolve().parent / "templates"),
)


def get_all_errors(outputs: Iterable[FileErrorOutput], /) -> Counter[FileError]:
    return Counter(output["error"] for output in outputs)


class UpstreamsTestOutput(TypedDict):
    collections: dict[CollectionName, list[FileErrorOutput]]


@dataclasses.dataclass()
class Args:
    data_path: Path
    tag_data_path: Path
    upstreams_data_path: Path

    @cached_property
    def data(self) -> SanityTestsOutput:
        data = load_yaml_file(self.data_path)
        data["collections"] = make_collection_mapping(data["collections"])
        return data

    @cached_property
    def tags_data(self) -> dict[CollectionName, CollectionTagData]:
        data = load_yaml_file(self.tag_data_path)
        data = make_collection_mapping(data)
        return data

    @cached_property
    def upstreams_data(self) -> UpstreamsTestOutput:
        data = load_yaml_file(self.upstreams_data_path)
        data["collections"] = make_collection_mapping(data["collections"])
        return data


@app.callback()
def callback(
    ctx: typer.Context,
    data_path: Path = typer.Option(..., "-i", "--data", "--sanity-data"),
    tag_data: Path = typer.Option(..., "-t", "--tag-data"),
    upstreams_data_path: Path = typer.Option(..., "-u", "--upstreams-data"),
):
    ctx.obj = Args(data_path, tag_data, upstreams_data_path)


def get_test_name(path: str) -> str:
    return path.removeprefix("ansible-test-sanity-").removesuffix(".json")


@app.command()
def render(ctx: typer.Context, collection_: str) -> None:
    sargs = ctx.ensure_object(Args)
    collection = CollectionName(collection_)
    rendered = render_issue(collection, sargs)
    print(rendered)


@app.command()
def issue(ctx: typer.Context, collection_: str) -> None:
    sargs = ctx.ensure_object(Args)
    collection = CollectionName(collection_)
    has_file_errors = collection in sargs.upstreams_data["collections"]
    title = "Community package requirements: sanity tests"
    if has_file_errors:
        title += " and repository management"
    body = render_issue(collection, sargs)

    # `repository` shouldn't be None, mypy.
    assert (u := sargs.tags_data[collection]["repository"])
    # Guess issue tracker URL. This won't always be correct, but close enough
    issue_url = URL(u) / "issues/new"
    issue_url = issue_url.with_query(title=title)

    # Clipboard managers will save both
    pyperclip.copy(title)
    pyperclip.copy(body)

    webbrowser.open(str(issue_url))


def render_issue(collection: CollectionName, sargs: Args) -> str:
    sanity_data = sargs.data["collections"][collection]
    test_json = sanity_data["sanity"]["test_json"]
    tags_data = sargs.tags_data[collection]
    file_errors = sargs.upstreams_data["collections"].get(collection) or []

    tvars = {
        "collection_name": collection,
        "test_json": test_json,
        "tag_output": tags_data,
        "file_errors": file_errors,
        "env_details": sargs.data["env_details"],
    }
    return env.get_template("issue.md").render(**tvars)


@app.command()
def failures(
    ctx: typer.Context,
) -> None:
    sargs = ctx.ensure_object(Args)
    upstreams_data = sargs.upstreams_data["collections"]
    failed_collectiions: dict[CollectionName, dict[str | FileError, int]] = defaultdict(
        dict,
        {
            collection: {
                get_test_name(name): sum(
                    len(r["output"].splitlines()) for r in test_json["results"]
                )
                for name, test_json in data["sanity"]["test_json"].items()
            }
            for collection, data in sargs.data["collections"].items()
            if data["failed"]
        },
    )
    for collection, upstream_data in upstreams_data.items():
        failed_collectiions[collection] |= cast(
            "dict[str | FileError, int]", get_all_errors(upstream_data)
        )
    for collection, test_data in sorted(
        failed_collectiions.items(), key=lambda x: sum(x[1].values())
    ):
        print("*", collection)
        for name, output_count in sorted(
            test_data.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"    {output_count} {name}")


if __name__ == "__main__":
    app()
