# Community package requirements: sanity tests and repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `24.6.1` of `awx.awx`, corresponding to the `24.6.1` tag in this repo, fails one or more of the required sanity tests.

The contents in the `24.6.1` git tag do not match `awx-awx-24.6.1.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.17.4`:

- ansible-doc
- compile
- validate-modules
- yamllint

Note that this is only a subset of the required sanity tests. Please make sure you run them in all in your CI.

### Results

`ansible-test sanity` succeeded, but some required tests were ignored.

### Invalid test ignores

`tests/sanity/ignore-2.17.txt` contain ignores that are forbidden by the [CI testing requirements][ci-testing]:

``` text
plugins/modules/export.py validate-modules:nonexistent-parameter-documented # needs awxkit to construct argspec
```

Please fix these issues and remove the ignore entries.

## File divergences

The following files differ between the `24.6.1` git tag and `awx-awx-24.6.1.tar.gz` on Ansible Galaxy:

- `plugins/module_utils/controller_api.py` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
