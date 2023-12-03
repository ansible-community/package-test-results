#!/usr/bin/env python3

# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: GPL-3.0-or-later
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import dataclasses
import webbrowser
from collections import Counter
from collections.abc import Iterable, Iterator
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict, cast

import jinja2
import pyperclip  # type: ignore[import]
import typer
from antsibull.sanity_tests import CollectionOutput, IgnoreEntry
from antsibull.types import CollectionName, make_collection_mapping
from antsibull_core.yaml import load_yaml_file, store_yaml_stream
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


def get_issue_title(collection: CollectionName, sargs: Args) -> str:
    has_sanity_errors = sargs.data["collections"][collection]["failed"]
    has_file_errors = collection in sargs.upstreams_data["collections"]
    title = "Community package requirements: "
    found: list[str] = []
    if has_sanity_errors:
        found.append("sanity tests")
    if has_file_errors:
        found.append("repository management")
    if not found:
        raise ValueError("No errors found")
    title += " and ".join(found)
    return title


@app.command()
def render(
    ctx: typer.Context,
    collection_: str,
    add_title: bool = typer.Option(False, "-T", "--add-title"),
    output: typer.FileTextWrite = typer.Option("-", "-o", "--output"),
) -> None:
    sargs = ctx.ensure_object(Args)
    collection = CollectionName(collection_)
    rendered = render_issue(collection, sargs)
    if add_title:
        title = get_issue_title(collection, sargs)
        rendered = f"# {title}\n\n" + rendered.lstrip("\n")
    print(rendered, file=output)
    output.close()


@app.command()
def render_all(
    ctx: typer.Context,
    output_dir: Path = typer.Option(..., "-O", "--output-dir"),
    add_title: bool = typer.Option(False, "-T", "--add-title"),
) -> None:
    sargs = ctx.ensure_object(Args)
    for collection, data in sargs.data["collections"].items():
        # fmt: off
        if (
            not data["failed"]
            and not sargs.upstreams_data["collections"].get(collection)
        ):
        # fmt: on
            continue
        render(
            ctx,
            collection,
            add_title,
            cast(typer.FileTextWrite, (output_dir / f"{collection}.md").open("w")),
        )


@app.command()
def sanity_data(
    ctx: typer.Context,
    collection_: str,
    output: typer.FileTextWrite = typer.Option("-", "-o", "--output"),
) -> None:
    sargs = ctx.ensure_object(Args)
    collection = CollectionName(collection_)
    data = sargs.data["collections"][collection]
    store_yaml_stream(output, data)
    output.close()


@app.command()
def issue(ctx: typer.Context, collection_: str) -> None:
    sargs = ctx.ensure_object(Args)
    collection = CollectionName(collection_)
    title = get_issue_title(collection, sargs)
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
    sanity = sanity_data["sanity"]
    test_json = sanity["test_json"]
    tags_data = sargs.tags_data[collection]
    file_errors = sargs.upstreams_data["collections"].get(collection) or []
    invalid_ignores = [
        IgnoreEntry(**data) for data in cast(dict, sanity["banned_ignore_entries"])
    ]

    tvars = {
        "collection_name": collection,
        "test_json": test_json,
        "invalid_ignores": invalid_ignores,
        "tag_output": tags_data,
        "file_errors": file_errors,
        "env_details": sargs.data["env_details"],
        "ignores_file": sanity.get("ignores_file"),
    }
    return env.get_template("issue.md").render(**tvars)


def get_error_tuples(
    sanity: CollectionOutput, upstreams: list[FileErrorOutput] | None
) -> Iterator[tuple[str | FileError, int]]:
    for file, test_json in sanity["sanity"]["test_json"].items():
        yield get_test_name(file), sum(
            len(r["output"].splitlines()) for r in test_json["results"]
        )
    if banned := sanity["sanity"].get("banned_ignore_entries"):
        yield "BANNED_SANITY", len(banned)
    if upstreams:
        yield from get_all_errors(upstreams).items()


@app.command()
def failures(
    ctx: typer.Context,
) -> None:
    sargs = ctx.ensure_object(Args)
    sanity = sargs.data["collections"]
    upstreams = sargs.upstreams_data["collections"]
    failed_collectiions: dict[CollectionName, dict[str | FileError, int]] = {
        collection: out
        for collection, sanity_out in sanity.items()
        if (out := dict(get_error_tuples(sanity_out, upstreams.get(collection))))
    }
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
