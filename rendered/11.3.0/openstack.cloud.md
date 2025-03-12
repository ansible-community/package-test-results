# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `2.4.1` of `openstack.cloud`, corresponding to the `2.4.1` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.18.3`:

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

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.18/dev_guide/testing/sanity/yamllint.html)] failed with 4 errors:

``` text
.zuul.yaml:268:14: unparsable-with-libyaml: None - could not determine a constructor for the tag '!encrypted/pkcs1-oaep'
ci/roles/quota/tasks/loadbalancer.yml:158:1: empty-lines: too many blank lines (1 > 0)
ci/roles/quota/tasks/main.yml:136:1: empty-lines: too many blank lines (1 > 0)
ci/roles/server_group/defaults/main.yml:11:1: empty-lines: too many blank lines (1 > 0)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
