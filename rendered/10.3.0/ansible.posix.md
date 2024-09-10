# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.5.4` of `ansible.posix`, corresponding to the `1.5.4` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.17.3`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.17/dev_guide/testing/sanity/validate-modules.html)] failed with 9 errors:

``` text
plugins/modules/synchronize.py:0:0: doc-default-does-not-match-spec: Argument '_local_rsync_path' in argument_spec defines default as ('rsync') but documentation defines default as (None)
plugins/modules/synchronize.py:0:0: doc-default-does-not-match-spec: Argument '_substitute_controller' in argument_spec defines default as (False) but documentation defines default as (None)
plugins/modules/synchronize.py:0:0: doc-default-does-not-match-spec: Argument 'rsync_opts' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/synchronize.py:0:0: nonexistent-parameter-documented: Argument 'use_ssh_args' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/synchronize.py:0:0: parameter-type-not-in-doc: Argument 'ssh_args' in argument_spec defines type as 'str' but documentation doesn't define type
plugins/modules/synchronize.py:0:0: undocumented-parameter: Argument '_local_rsync_password' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/synchronize.py:0:0: undocumented-parameter: Argument '_local_rsync_path' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/synchronize.py:0:0: undocumented-parameter: Argument '_substitute_controller' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/synchronize.py:0:0: undocumented-parameter: Argument 'ssh_args' is listed in the argument_spec, but not documented in the module documentation
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
