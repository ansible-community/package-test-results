# Community package requirements: sanity tests and repository management

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.14.0` of `sensu.sensu_go`, corresponding to the `v1.14.0` tag in this repo, fails one or more of the required sanity tests.

The contents in the `v1.14.0` git tag do not match `sensu-sensu_go-1.14.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.16.0`:

- ansible-doc
- compile
- validate-modules
- yamllint

Note that this is only a subset of the required sanity tests. Please make sure you run them in all in your CI.

### Results

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 7 errors:

``` text
plugins/modules/bonsai_asset.py:0:0: nonexistent-parameter-documented: Argument 'annotations' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/bonsai_asset.py:0:0: nonexistent-parameter-documented: Argument 'auth' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/bonsai_asset.py:0:0: nonexistent-parameter-documented: Argument 'labels' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/bonsai_asset.py:0:0: nonexistent-parameter-documented: Argument 'namespace' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/bonsai_asset.py:0:0: nonexistent-parameter-documented: Argument 'on_remote' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/bonsai_asset.py:0:0: nonexistent-parameter-documented: Argument 'rename' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/datastore.py:0:0: doc-default-does-not-match-spec: Argument 'pool_size' in argument_spec defines default as (0) but documentation defines default as (None)
```



## File divergences

The following files differ between the `v1.14.0` git tag and `sensu-sensu_go-1.14.0.tar.gz` on Ansible Galaxy:

- `docs/source/release_notes.rst` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
