# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `21.7.1` of `netapp.aws`, corresponding to the `21.7.1` tag in this repo, fails one or more of the required sanity tests.


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

> **💡 NOTE:**
>
> Check the `[explain]` links below for more information about each test and how to fix failures.
> See [Sanity Tests: Ignores](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/ignores.html) in the dev guide if, after reading the test-specific documentation, you still believe an error is a false positive.

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 4 errors:

``` text
plugins/modules/aws_netapp_cvs_active_directory.py:0:0: doc-default-does-not-match-spec: Argument 'feature_flags' in argument_spec defines default as ({}) but documentation defines default as (None)
plugins/modules/aws_netapp_cvs_filesystems.py:0:0: doc-default-does-not-match-spec: Argument 'feature_flags' in argument_spec defines default as ({}) but documentation defines default as (None)
plugins/modules/aws_netapp_cvs_pool.py:0:0: doc-default-does-not-match-spec: Argument 'feature_flags' in argument_spec defines default as ({}) but documentation defines default as (None)
plugins/modules/aws_netapp_cvs_snapshots.py:0:0: doc-default-does-not-match-spec: Argument 'feature_flags' in argument_spec defines default as ({}) but documentation defines default as (None)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
