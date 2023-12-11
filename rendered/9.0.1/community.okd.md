# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `2.3.0` of `community.okd`, corresponding to the `2.3.0` tag in this repo, fails one or more of the required sanity tests.


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
plugins/modules/k8s.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7fb27a67fd80> but documentation doesn't define type
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.error.contains: required key not provided @ data['result']['contains']['error']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.metadata.contains: required key not provided @ data['result']['contains']['metadata']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.spec.contains: required key not provided @ data['result']['contains']['spec']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.status.contains: required key not provided @ data['result']['contains']['status']['contains']. Got None
plugins/modules/openshift_process.py:0:0: parameter-type-not-in-doc: Argument 'namespace_target' in argument_spec defines type as 'str' but documentation doesn't define type
plugins/modules/openshift_process.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7fb27a67fd80> but documentation doesn't define type
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
