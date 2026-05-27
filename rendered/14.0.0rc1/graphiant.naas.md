# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `26.4.0` of `graphiant.naas`, corresponding to the `v26.4.0` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.21/dev_guide/testing/sanity/yamllint.html)] failed with 25 errors:

``` text
configs/de_workflows_configs/sample_data_exchange_acceptance_scale2.yaml:14:4: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
configs/de_workflows_configs/sample_data_exchange_customers_scale2.yaml:11:4: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
configs/de_workflows_configs/sample_data_exchange_matches_scale2.yaml:18:4: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
configs/de_workflows_configs/sample_global_lan_segments2.yaml:4:4: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/bgp_peering_template.yaml:3:6: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/circuit_template.yaml:4:10: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/data_exchange_acceptance_template.yaml:95:53: unparsable-with-libyaml: while parsing a flow mapping did not find expected ',' or '}'
templates/data_exchange_customer_template.yaml:8:16: unparsable-with-libyaml: while constructing a mapping found unhashable key
templates/data_exchange_match_template.yaml:5:6: unparsable-with-libyaml: while constructing a mapping found unhashable key
templates/data_exchange_service_template.yaml:8:23: unparsable-with-libyaml: while constructing a mapping found unhashable key
templates/device_config_template.yaml:25:2: error: syntax error: found character '%' that cannot start any token (syntax)
templates/device_config_template.yaml:25:2: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/device_config_template.yaml:50:1: empty-lines: too many blank lines (1 > 0)
templates/global_bgp_routing_policies_template.yaml:4:10: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/global_graphiant_routing_policies_template.yaml:8:10: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/global_ipfix_template.yaml:9:18: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/global_prefix_set_template.yaml:4:10: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/global_site_lists_template.yaml:7:8: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/global_snmps_template.yaml:6:14: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/global_syslog_template.yaml:7:22: unparsable-with-libyaml: while constructing a mapping found unhashable key
templates/global_vpn_profile_template.yaml:4:10: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/interface_template.yaml:13:18: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/lag_interfaces_template.yaml:2:6: error: syntax error: found character '%' that cannot start any token (syntax)
templates/lag_interfaces_template.yaml:2:6: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
templates/vrrp_interfaces_template.yaml:6:18: unparsable-with-libyaml: while scanning for the next token found character that cannot start any token
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
