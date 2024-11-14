# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.7.8` of `community.mongodb`, corresponding to the `1.7.8` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.18.0`:

- ansible-doc
- compile
- validate-modules
- yamllint

Note that this is only a subset of the required sanity tests. Please make sure you run them in all in your CI.

### Results

> **💡 NOTE:**
>
> Check the `[explain]` links below for more information about each test and how to fix failures.
> See [Sanity Tests: Ignores](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/ignores.html) in the dev guide if, after reading the test-specific documentation, you still believe an error is a false positive.

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.18/dev_guide/testing/sanity/validate-modules.html)] failed with 1 error:

``` text
plugins/modules/mongodb_shell.py:0:0: import-error: Exception attempting to import module for argument_spec introspection, 'No module named 'pipes''
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.18/dev_guide/testing/sanity/yamllint.html)] failed with 2 errors:

``` text
tests/ansible-operator/config/manager/manager.yaml:1:1: multiple-yaml-documents: expected a single document in the stream
tests/ansible-operator/roles/create-certificates/templates/certificate.yaml:8:15: unparsable-with-libyaml: while constructing a mapping - found unhashable key
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
