# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.20.1` of `containers.podman`, corresponding to the `1.20.1` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.21.0`:

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

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.21/dev_guide/testing/sanity/yamllint.html)] failed with 8 errors:

``` text
.github/actions/setup-ansible-collection/action.yml:54:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/build_ai_env_with_ansible.yml:41:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/build_go_ai_multistage.yml:84:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/build_node_ai_api.yml:76:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/podman_copy_fetch.yml:40:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/podman_exec_basic.yml:27:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/podman_multiuser_tasks.yml:37:1: empty-lines: too many blank lines (2 > 0)
playbooks/examples/podman_pkg_manage.yml:40:1: empty-lines: too many blank lines (2 > 0)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
