# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `4.0.1` of `community.okd`, corresponding to the `4.0.1` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.19.0b1`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/devel/dev_guide/testing/sanity/validate-modules.html)] failed with 6 errors:

``` text
plugins/modules/k8s.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7f008179f740> but documentation doesn't define type
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.error.contains: required key not provided @ data['result']['contains']['error']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.metadata.contains: required key not provided @ data['result']['contains']['metadata']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.spec.contains: required key not provided @ data['result']['contains']['spec']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.status.contains: required key not provided @ data['result']['contains']['status']['contains']. Got None
plugins/modules/openshift_process.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7f008179f740> but documentation doesn't define type
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
