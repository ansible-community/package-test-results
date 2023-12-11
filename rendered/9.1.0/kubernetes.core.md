# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `2.4.0` of `kubernetes.core`, corresponding to the `2.4.0` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 25 errors:

``` text
plugins/modules/helm_info.py:0:0: doc-default-does-not-match-spec: Argument 'release_state' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/helm_template.py:0:0: doc-default-does-not-match-spec: Argument 'show_only' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7f8121010180> but documentation doesn't define type
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.error.contains: required key not provided @ data['result']['contains']['error']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.metadata.contains: required key not provided @ data['result']['contains']['metadata']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.spec.contains: required key not provided @ data['result']['contains']['spec']['contains']. Got None
plugins/modules/k8s.py:0:0: return-syntax-error: RETURN.result.contains.status.contains: required key not provided @ data['result']['contains']['status']['contains']. Got None
plugins/modules/k8s_drain.py:0:0: doc-default-does-not-match-spec: Argument 'delete_options' in argument_spec defines default as ({}) but documentation defines default as (None)
plugins/modules/k8s_info.py:0:0: doc-default-does-not-match-spec: Argument 'field_selectors' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s_info.py:0:0: doc-default-does-not-match-spec: Argument 'label_selectors' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s_log.py:0:0: doc-default-does-not-match-spec: Argument 'label_selectors' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s_rollback.py:0:0: doc-default-does-not-match-spec: Argument 'field_selectors' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s_rollback.py:0:0: doc-default-does-not-match-spec: Argument 'label_selectors' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s_scale.py:0:0: doc-default-does-not-match-spec: Argument 'label_selectors' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/k8s_scale.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7f8121010180> but documentation doesn't define type
plugins/modules/k8s_scale.py:0:0: return-syntax-error: RETURN.result.contains.metadata.contains: required key not provided @ data['result']['contains']['metadata']['contains']. Got None
plugins/modules/k8s_scale.py:0:0: return-syntax-error: RETURN.result.contains.spec.contains: required key not provided @ data['result']['contains']['spec']['contains']. Got None
plugins/modules/k8s_scale.py:0:0: return-syntax-error: RETURN.result.contains.status.contains: required key not provided @ data['result']['contains']['status']['contains']. Got None
plugins/modules/k8s_service.py:0:0: parameter-type-not-in-doc: Argument 'resource_definition' in argument_spec defines type as <function list_dict_str at 0x7f8121010180> but documentation doesn't define type
plugins/modules/k8s_service.py:0:0: return-syntax-error: RETURN.result.contains.metadata.contains: required key not provided @ data['result']['contains']['metadata']['contains']. Got None
plugins/modules/k8s_service.py:0:0: return-syntax-error: RETURN.result.contains.spec.contains: required key not provided @ data['result']['contains']['spec']['contains']. Got None
plugins/modules/k8s_service.py:0:0: return-syntax-error: RETURN.result.contains.status.contains: required key not provided @ data['result']['contains']['status']['contains']. Got None
plugins/modules/k8s_taint.py:0:0: return-syntax-error: RETURN.result.contains.metadata.contains: required key not provided @ data['result']['contains']['metadata']['contains']. Got None
plugins/modules/k8s_taint.py:0:0: return-syntax-error: RETURN.result.contains.spec.contains: required key not provided @ data['result']['contains']['spec']['contains']. Got None
plugins/modules/k8s_taint.py:0:0: return-syntax-error: RETURN.result.contains.status.contains: required key not provided @ data['result']['contains']['status']['contains']. Got None
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/yamllint.html)] failed with 9 errors:

``` text
tests/integration/targets/helm/files/appversionless-chart-v2/templates/configmap.yaml:6:13: unparsable-with-libyaml: while constructing a mapping - found unhashable key
tests/integration/targets/helm/files/appversionless-chart/templates/configmap.yaml:6:13: unparsable-with-libyaml: while constructing a mapping - found unhashable key
tests/integration/targets/helm/files/test-chart-v2/templates/configmap.yaml:6:13: unparsable-with-libyaml: while constructing a mapping - found unhashable key
tests/integration/targets/helm/files/test-chart/templates/configmap.yaml:6:13: unparsable-with-libyaml: while constructing a mapping - found unhashable key
tests/integration/targets/helm_diff/files/test-chart/templates/configmap.yaml:6:13: unparsable-with-libyaml: while constructing a mapping - found unhashable key
tests/integration/targets/k8s_scale/files/deployment.yaml:26:1: unparsable-with-libyaml: expected a single document in the stream - but found another document
tests/unit/module_utils/fixtures/definitions.yml:6:1: unparsable-with-libyaml: expected a single document in the stream - but found another document
tests/unit/module_utils/fixtures/deployments.yml:25:1: unparsable-with-libyaml: expected a single document in the stream - but found another document
tests/unit/module_utils/fixtures/pods.yml:18:1: unparsable-with-libyaml: expected a single document in the stream - but found another document
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
