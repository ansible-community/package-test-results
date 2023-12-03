# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.27.0` of `f5networks.f5_modules`, corresponding to the `1.27.0` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 175 errors:

``` text
plugins/lookup/bigiq_license.py:0:0: invalid-documentation: DOCUMENTATION.author: Invalid author for dictionary value @ data['author']. Got 'Wojciech Wypior <w.wypior@f5.com>'
plugins/lookup/bigiq_license.py:0:0: invalid-documentation: DOCUMENTATION.lookup: extra keys not allowed @ data['lookup']. Got 'bigiq_license'
plugins/lookup/bigiq_license.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/license_hopper.py:0:0: invalid-documentation: DOCUMENTATION.author: Invalid author for dictionary value @ data['author']. Got 'Tim Rupp <caphrim007@gmail.com>'
plugins/lookup/license_hopper.py:0:0: invalid-documentation: DOCUMENTATION.lookup: extra keys not allowed @ data['lookup']. Got 'Select a random license key from a file and remove it from future lookups'
plugins/lookup/license_hopper.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/modules/bigip_data_group.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in records
plugins/modules/bigip_device_auth_ldap.py:0:0: no-log-needed: Argument 'client_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_device_license.py:0:0: no-log-needed: Argument 'addon_keys' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_device_license.py:0:0: no-log-needed: Argument 'license_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_dns_nameserver.py:0:0: no-log-needed: Argument 'tsig_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_dns_zone.py:0:0: no-log-needed: Argument 'tsig_server_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_firewall_address_list.py:0:0: doc-choices-do-not-match-spec: Argument 'country' in argument_spec found in geo_locations defines choices as ([]) but documentation defines choices as (['Any valid 2 character ISO country code.', 'Any valid country name.'])
plugins/modules/bigip_firewall_log_profile_network.py:0:0: implied-parameter-type-mismatch: Argument 'rate_limit' in argument_spec found in log_ip_errors implies type as 'str' but documentation defines as 'int'
plugins/modules/bigip_firewall_log_profile_network.py:0:0: implied-parameter-type-mismatch: Argument 'rate_limit' in argument_spec found in log_matches_accept_rule implies type as 'str' but documentation defines as 'int'
plugins/modules/bigip_firewall_log_profile_network.py:0:0: implied-parameter-type-mismatch: Argument 'rate_limit' in argument_spec found in log_matches_drop_rule implies type as 'str' but documentation defines as 'int'
plugins/modules/bigip_firewall_log_profile_network.py:0:0: implied-parameter-type-mismatch: Argument 'rate_limit' in argument_spec found in log_matches_reject_rule implies type as 'str' but documentation defines as 'int'
plugins/modules/bigip_firewall_log_profile_network.py:0:0: implied-parameter-type-mismatch: Argument 'rate_limit' in argument_spec found in log_tcp_errors implies type as 'str' but documentation defines as 'int'
plugins/modules/bigip_firewall_log_profile_network.py:0:0: implied-parameter-type-mismatch: Argument 'rate_limit' in argument_spec found in log_tcp_events implies type as 'str' but documentation defines as 'int'
plugins/modules/bigip_gtm_monitor_https.py:0:0: no-log-needed: Argument 'client_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-choices-do-not-match-spec: Argument 'state' in argument_spec found in aggregate defines choices as (['present', 'absent', 'disabled', 'enabled']) but documentation defines choices as ([])
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-missing-type: Argument 'description' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-missing-type: Argument 'monitor' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-missing-type: Argument 'partition' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-missing-type: Argument 'server_name' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-missing-type: Argument 'state' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: doc-missing-type: Argument 'virtual_server' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: missing-suboption-docs: Argument 'aggregate' in argument_spec has sub-options but documentation does not define it
plugins/modules/bigip_gtm_pool_member.py:0:0: missing-suboption-docs: Argument 'limits' in argument_spec found in aggregate has sub-options but documentation does not define it
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'bits_enabled' in argument_spec found in aggregate -> limits defines type as 'bool' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'bits_limit' in argument_spec found in aggregate -> limits defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'connections_enabled' in argument_spec found in aggregate -> limits defines type as 'bool' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'connections_limit' in argument_spec found in aggregate -> limits defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'limits' in argument_spec found in aggregate defines type as 'dict' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'member_order' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'packets_enabled' in argument_spec found in aggregate -> limits defines type as 'bool' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'packets_limit' in argument_spec found in aggregate -> limits defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'ratio' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'bits_enabled' found in aggregate -> limits is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'bits_limit' found in aggregate -> limits is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'connections_enabled' found in aggregate -> limits is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'connections_limit' found in aggregate -> limits is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'description' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'limits' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'member_order' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'monitor' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'packets_enabled' found in aggregate -> limits is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'packets_limit' found in aggregate -> limits is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'partition' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'ratio' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'server_name' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'state' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_gtm_pool_member.py:0:0: undocumented-parameter: Argument 'virtual_server' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_ike_peer.py:0:0: no-log-needed: Argument 'phase1_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_imish_config.py:0:0: incompatible-default-type: DOCUMENTATION.options.route_domain: Argument defines default as (0) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['route_domain']. Got {'description': ['Route domain on which to manage the BGP configuration.'], 'type': 'str', 'default': 0}
plugins/modules/bigip_password_policy.py:0:0: no-log-needed: Argument 'password_memory' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_pool.py:0:0: doc-choices-do-not-match-spec: Argument 'lb_method' in argument_spec found in aggregate defines choices as (['dynamic-ratio-member', 'dynamic-ratio-node', 'fastest-app-response', 'fastest-node', 'least-connections-member', 'least-connections-node', 'least-sessions', 'observed-member', 'observed-node', 'predictive-member', 'predictive-node', 'ratio-least-connections-member', 'ratio-least-connections-node', 'ratio-member', 'ratio-node', 'ratio-session', 'round-robin', 'weighted-least-connections-member', 'weighted-least-connections-node']) but documentation defines choices as ([])
plugins/modules/bigip_pool.py:0:0: doc-choices-do-not-match-spec: Argument 'min_up_members_action' in argument_spec found in aggregate defines choices as (['failover', 'reboot', 'restart-all']) but documentation defines choices as ([])
plugins/modules/bigip_pool.py:0:0: doc-choices-do-not-match-spec: Argument 'min_up_members_checking' in argument_spec found in aggregate defines choices as (['enabled', 'disabled']) but documentation defines choices as ([])
plugins/modules/bigip_pool.py:0:0: doc-choices-do-not-match-spec: Argument 'monitor_type' in argument_spec found in aggregate defines choices as (['and_list', 'm_of_n', 'single']) but documentation defines choices as ([])
plugins/modules/bigip_pool.py:0:0: doc-choices-do-not-match-spec: Argument 'service_down_action' in argument_spec found in aggregate defines choices as (['none', 'reset', 'drop', 'reselect']) but documentation defines choices as ([])
plugins/modules/bigip_pool.py:0:0: doc-choices-do-not-match-spec: Argument 'state' in argument_spec found in aggregate defines choices as (['present', 'absent']) but documentation defines choices as ([])
plugins/modules/bigip_pool.py:0:0: doc-elements-mismatch: Argument 'monitors' in argument_spec found in aggregate specifies elements as str,but elements is not documented
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'description' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'lb_method' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'min_up_members_action' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'min_up_members_checking' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'monitor_type' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'name' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'partition' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'service_down_action' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: doc-missing-type: Argument 'state' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: missing-suboption-docs: Argument 'aggregate' in argument_spec has sub-options but documentation does not define it
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'metadata' in argument_spec found in aggregate defines type as 'raw' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'min_up_members' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'monitors' in argument_spec found in aggregate defines type as 'list' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'priority_group_activation' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'quorum' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'reselect_tries' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: parameter-type-not-in-doc: Argument 'slow_ramp_time' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'availability_requirements_at_least' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'availability_requirements_type' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'description' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'lb_method' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'metadata' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'min_up_members' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'min_up_members_action' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'min_up_members_checking' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'minimum_active_members' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'monitor_type' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'monitors' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'name' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'partition' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'pool' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'priority_group_activation' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'quorum' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'reselect_tries' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'service_down_action' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'slow_ramp_time' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool.py:0:0: undocumented-parameter: Argument 'state' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: doc-choices-do-not-match-spec: Argument 'state' in argument_spec found in aggregate defines choices as (['absent', 'present', 'enabled', 'disabled', 'forced_offline']) but documentation defines choices as ([])
plugins/modules/bigip_pool_member.py:0:0: doc-choices-do-not-match-spec: Argument 'type' in argument_spec found in aggregate -> availability_requirements defines choices as (['all', 'at_least']) but documentation defines choices as ([])
plugins/modules/bigip_pool_member.py:0:0: doc-elements-mismatch: Argument 'monitors' in argument_spec found in aggregate specifies elements as str,but elements is not documented
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'address' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'description' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'fqdn' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'ip_encapsulation' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'name' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'partition' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'state' in argument_spec found in aggregate uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-missing-type: Argument 'type' in argument_spec found in aggregate -> availability_requirements uses default type ('str') but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: doc-required-mismatch: Argument 'type' in argument_spec found in aggregate -> availability_requirements is required, but is not documented as being required
plugins/modules/bigip_pool_member.py:0:0: missing-suboption-docs: Argument 'aggregate' in argument_spec has sub-options but documentation does not define it
plugins/modules/bigip_pool_member.py:0:0: missing-suboption-docs: Argument 'availability_requirements' in argument_spec found in aggregate has sub-options but documentation does not define it
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'at_least' in argument_spec found in aggregate -> availability_requirements defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'availability_requirements' in argument_spec found in aggregate defines type as 'dict' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'connection_limit' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'fqdn_auto_populate' in argument_spec found in aggregate defines type as 'bool' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'monitors' in argument_spec found in aggregate defines type as 'list' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'port' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'preserve_node' in argument_spec found in aggregate defines type as 'bool' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'priority_group' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'rate_limit' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'ratio' in argument_spec found in aggregate defines type as 'int' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: parameter-type-not-in-doc: Argument 'reuse_nodes' in argument_spec found in aggregate defines type as 'bool' but documentation doesn't define type
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'address' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'at_least' found in aggregate -> availability_requirements is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'availability_requirements' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'connection_limit' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'description' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'fqdn' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'fqdn_auto_populate' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'host' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'hostname' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'ip' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'ip_encapsulation' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'monitors' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'name' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'partition' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'port' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'preserve_node' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'priority_group' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'rate_limit' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'ratio' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'reuse_nodes' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'state' found in aggregate is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_pool_member.py:0:0: undocumented-parameter: Argument 'type' found in aggregate -> availability_requirements is listed in the argument_spec, but not documented in the module documentation
plugins/modules/bigip_profile_client_ssl.py:0:0: no-log-needed: Argument 'cert_key_chain' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_profile_client_ssl.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in cert_key_chain
plugins/modules/bigip_profile_client_ssl.py:0:0: no-log-needed: Argument 'passphrase' in argument_spec could be a secret, though doesn't have `no_log` set found in cert_key_chain
plugins/modules/bigip_profile_server_ssl.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_ssl_ocsp.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_sys_db.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigip_tunnel.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/bigiq_application_fasthttp.py:0:0: incompatible-default-type: DOCUMENTATION.options.inbound_virtual.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['inbound_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(80).'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_fasthttp.py:0:0: incompatible-default-type: DOCUMENTATION.options.servers.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['servers']['suboptions']['port']. Got {'description': ['The port of the server.', 'When creating a new application and specifying a server, if this parameter is not provided, the default is C(80).'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_fastl4_tcp.py:0:0: incompatible-default-type: DOCUMENTATION.options.inbound_virtual.suboptions.port: Argument defines default as (8080) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['inbound_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(8080).'], 'type': 'str', 'default': 8080}
plugins/modules/bigiq_application_fastl4_tcp.py:0:0: incompatible-default-type: DOCUMENTATION.options.servers.suboptions.port: Argument defines default as (8000) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['servers']['suboptions']['port']. Got {'description': ['The port of the server.', 'When creating a new application and specifying a server, if this parameter is not provided, the default is C(8000).'], 'type': 'str', 'default': 8000}
plugins/modules/bigiq_application_fastl4_udp.py:0:0: incompatible-default-type: DOCUMENTATION.options.inbound_virtual.suboptions.port: Argument defines default as (53) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['inbound_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(53).'], 'type': 'str', 'default': 53}
plugins/modules/bigiq_application_fastl4_udp.py:0:0: incompatible-default-type: DOCUMENTATION.options.servers.suboptions.port: Argument defines default as (8000) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['servers']['suboptions']['port']. Got {'description': ['The port of the server.', 'When creating a new application and specifying a server, if this parameter is not provided, the default is C(8000).'], 'type': 'str', 'default': 8000}
plugins/modules/bigiq_application_http.py:0:0: incompatible-default-type: DOCUMENTATION.options.inbound_virtual.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['inbound_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(80).'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_http.py:0:0: incompatible-default-type: DOCUMENTATION.options.servers.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['servers']['suboptions']['port']. Got {'description': ['The port of the server.', 'When creating a new application and specifying a server, if this parameter is not provided, the default is C(80).'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_https_offload.py:0:0: incompatible-default-type: DOCUMENTATION.options.inbound_virtual.suboptions.port: Argument defines default as (443) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['inbound_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(443).'], 'type': 'str', 'default': 443}
plugins/modules/bigiq_application_https_offload.py:0:0: incompatible-default-type: DOCUMENTATION.options.redirect_virtual.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['redirect_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(80).'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_https_offload.py:0:0: incompatible-default-type: DOCUMENTATION.options.servers.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['servers']['suboptions']['port']. Got {'description': ['The port of the server.'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_https_offload.py:0:0: no-log-needed: Argument 'cert_key_chain' in argument_spec could be a secret, though doesn't have `no_log` set found in client_ssl_profile
plugins/modules/bigiq_application_https_offload.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in client_ssl_profile -> cert_key_chain
plugins/modules/bigiq_application_https_offload.py:0:0: no-log-needed: Argument 'passphrase' in argument_spec could be a secret, though doesn't have `no_log` set found in client_ssl_profile -> cert_key_chain
plugins/modules/bigiq_application_https_waf.py:0:0: incompatible-default-type: DOCUMENTATION.options.inbound_virtual.suboptions.port: Argument defines default as (443) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['inbound_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value is C(443).'], 'type': 'str', 'default': 443}
plugins/modules/bigiq_application_https_waf.py:0:0: incompatible-default-type: DOCUMENTATION.options.redirect_virtual.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['redirect_virtual']['suboptions']['port']. Got {'description': ['The port on which the virtual listens for connections.', 'When creating a new application, if this parameter is not specified, the default value of C(80) will be used.'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_https_waf.py:0:0: incompatible-default-type: DOCUMENTATION.options.servers.suboptions.port: Argument defines default as (80) but this is incompatible with parameter type str: Value must be string for dictionary value @ data['options']['servers']['suboptions']['port']. Got {'description': ['The port of the server.'], 'type': 'str', 'default': 80}
plugins/modules/bigiq_application_https_waf.py:0:0: no-log-needed: Argument 'cert_key_chain' in argument_spec could be a secret, though doesn't have `no_log` set found in client_ssl_profile
plugins/modules/bigiq_application_https_waf.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in client_ssl_profile -> cert_key_chain
plugins/modules/bigiq_application_https_waf.py:0:0: no-log-needed: Argument 'passphrase' in argument_spec could be a secret, though doesn't have `no_log` set found in client_ssl_profile -> cert_key_chain
plugins/modules/bigiq_regkey_license.py:0:0: no-log-needed: Argument 'regkey_pool' in argument_spec could be a secret, though doesn't have `no_log` set
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
