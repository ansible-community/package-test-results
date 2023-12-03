# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.0.2` of `gluster.gluster`, corresponding to the `1.0.2` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 10 errors:

``` text
plugins/modules/gluster_heal_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gluster_peer.py:0:0: doc-default-does-not-match-spec: Argument 'force' in argument_spec defines default as (None) but documentation defines default as (False)
plugins/modules/gluster_peer.py:0:0: doc-required-mismatch: Argument 'state' in argument_spec is not required, but is documented as being required
plugins/modules/gluster_peer.py:0:0: no-default-for-required-parameter: DOCUMENTATION.options.state: Argument is marked as required but specifies a default. Arguments with a default should not be marked as required for dictionary value @ data['options']['state']. Got {'choices': ['present', 'absent'], 'default': 'present', 'description': ['Determines whether the nodes should be attached to the pool or removed from the pool. If the state is present, nodes will be attached to the pool. If state is absent, nodes will be detached from the pool.'], 'required': True, 'type': 'str'}
plugins/modules/gluster_peer.py:0:0: parameter-list-no-elements: Argument 'nodes' in argument_spec defines type as list but elements is not defined
plugins/modules/gluster_peer.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.nodes: Argument defines type as list but elements is not defined for dictionary value @ data['options']['nodes']. Got {'description': ['List of nodes that have to be probed into the pool.'], 'required': True, 'type': 'list'}
plugins/modules/gluster_volume.py:0:0: doc-default-does-not-match-spec: Argument 'force' in argument_spec defines default as (False) but documentation defines default as (None)
plugins/modules/gluster_volume.py:0:0: doc-default-does-not-match-spec: Argument 'options' in argument_spec defines default as ({}) but documentation defines default as (None)
plugins/modules/gluster_volume.py:0:0: parameter-list-no-elements: Argument 'cluster' in argument_spec defines type as list but elements is not defined
plugins/modules/gluster_volume.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.cluster: Argument defines type as list but elements is not defined for dictionary value @ data['options']['cluster']. Got {'description': ['List of hosts to use for probing and brick setup.'], 'type': 'list'}
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
