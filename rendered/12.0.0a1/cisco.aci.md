# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `2.10.1` of `cisco.aci`, corresponding to the `v2.10.1` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/devel/dev_guide/testing/sanity/validate-modules.html)] failed with 16 errors:

``` text
plugins/modules/aci_cloud_subnet.py:0:0: parameter-documented-aliases-differ: Argument 'address' in argument_spec has names 'address', but its documentation has names 'address', 'subnet'
plugins/modules/aci_cloud_subnet.py:0:0: parameter-documented-aliases-differ: Argument 'name' in argument_spec has names 'name', 'subnet', but its documentation has names 'name'
plugins/modules/aci_interface_policy_hsrp.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_tenant'
plugins/modules/aci_l2out_logical_interface_path.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l2out'
plugins/modules/aci_l2out_logical_interface_profile.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l2out'
plugins/modules/aci_l2out_logical_node_profile.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l2out'
plugins/modules/aci_l3out_bgp_peer.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l3out'
plugins/modules/aci_l3out_extsubnet.py:0:0: parameter-documented-aliases-differ: Argument 'extepg' in argument_spec has names 'extepg', 'extepg_name', 'name', but its documentation has names 'extepg', 'extepg_name'
plugins/modules/aci_l3out_hsrp_group.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_tenant'
plugins/modules/aci_l3out_hsrp_interface_profile.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_tenant'
plugins/modules/aci_l3out_hsrp_secondary_vip.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_tenant'
plugins/modules/aci_l3out_interface.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_tenant'
plugins/modules/aci_l3out_interface_secondary_ip.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l3out'
plugins/modules/aci_l3out_logical_node.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l3out'
plugins/modules/aci_l3out_logical_node_profile.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l3out'
plugins/modules/aci_l3out_static_routes_nexthop.py:0:0: invalid-documentation: DOCUMENTATION.seealso.0.module: Module/plugin name must be of format `<namespace>.<collection>.<name>(.<subname>)*` for dictionary value @ data['seealso'][0]['module']. Got 'aci_l3out'
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
