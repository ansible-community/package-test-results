# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `3.8.0` of `community.mysql`, corresponding to the `3.8.0` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.16.1`:

- ansible-doc
- compile
- validate-modules
- yamllint

Note that this is only a subset of the required sanity tests. Please make sure you run them in all in your CI.

### Results

`ansible-test sanity` succeeded, but some required tests were ignored.

### Invalid test ignores

`tests/sanity/ignore-2.16.txt` contain ignores that are forbidden by the [CI testing requirements][ci-testing]:

``` text
plugins/modules/mysql_db.py validate-modules:parameter-list-no-elements
plugins/modules/mysql_info.py validate-modules:parameter-list-no-elements
plugins/modules/mysql_query.py validate-modules:parameter-list-no-elements
plugins/modules/mysql_variables.py validate-modules:doc-required-mismatch
```

Please fix these issues and remove the ignore entries.


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
