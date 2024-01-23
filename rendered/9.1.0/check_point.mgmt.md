# Community package requirements: sanity tests and repository management

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `5.1.1` of `check_point.mgmt`, corresponding to the `v5.1.1` tag in this repo, fails one or more of the required sanity tests.

The contents in the `v5.1.1` git tag do not match `check_point-mgmt-5.1.1.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

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

> **💡 NOTE:**
>
> Check the `[explain]` links below for more information about each test and how to fix failures.
> See [Sanity Tests: Ignores](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/ignores.html) in the dev guide if, after reading the test-specific documentation, you still believe an error is a false positive.

The test `ansible-test sanity --test ansible-doc` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/ansible-doc.html)] failed with the error:

``` text
Command "ansible-doc -t module check_point.mgmt.cp_mgmt_abort_get_interfaces check_point.mgmt.cp_mgmt_access_layer check_point.mgmt.cp_mgmt_access_layer_facts check_point.mgmt.cp_mgmt_access_layers check_point.mgmt.cp_mgmt_access_point_name check_point.mgmt.cp_mgmt_access_point_name_facts check_point.mgmt.cp_mgmt_access_role check_point.mgmt.cp_mgmt_access_role_facts check_point.mgmt.cp_mgmt_access_rule check_point.mgmt.cp_mgmt_access_rule_facts check_point.mgmt.cp_mgmt_access_rules check_point.mgmt.cp_mgmt_access_section check_point.mgmt.cp_mgmt_add_api_key check_point.mgmt.cp_mgmt_add_data_center_object check_point.mgmt.cp_mgmt_add_domain check_point.mgmt.cp_mgmt_add_nat_rule check_point.mgmt.cp_mgmt_add_repository_package check_point.mgmt.cp_mgmt_add_rules_batch check_point.mgmt.cp_mgmt_add_updatable_object check_point.mgmt.cp_mgmt_address_range check_point.mgmt.cp_mgmt_address_range_facts check_point.mgmt.cp_mgmt_administrator check_point.mgmt.cp_mgmt_administrator_facts check_point.mgmt.cp_mgmt_application_site check_point.mgmt.cp_mgmt_application_site_category check_point.mgmt.cp_mgmt_application_site_category_facts check_point.mgmt.cp_mgmt_application_site_facts check_point.mgmt.cp_mgmt_application_site_group check_point.mgmt.cp_mgmt_application_site_group_facts check_point.mgmt.cp_mgmt_approve_session check_point.mgmt.cp_mgmt_assign_global_assignment check_point.mgmt.cp_mgmt_check_network_feed check_point.mgmt.cp_mgmt_check_threat_ioc_feed check_point.mgmt.cp_mgmt_checkpoint_host check_point.mgmt.cp_mgmt_checkpoint_host_facts check_point.mgmt.cp_mgmt_cluster_members_facts check_point.mgmt.cp_mgmt_connect_cloud_services check_point.mgmt.cp_mgmt_data_center_object_facts check_point.mgmt.cp_mgmt_delete_api_key check_point.mgmt.cp_mgmt_delete_data_center_object check_point.mgmt.cp_mgmt_delete_domain check_point.mgmt.cp_mgmt_delete_nat_rule check_point.mgmt.cp_mgmt_delete_repository_package check_point.mgmt.cp_mgmt_delete_rules_batch check_point.mgmt.cp_mgmt_delete_updatable_object check_point.mgmt.cp_mgmt_discard check_point.mgmt.cp_mgmt_disconnect_cloud_services check_point.mgmt.cp_mgmt_dns_domain check_point.mgmt.cp_mgmt_dns_domain_facts check_point.mgmt.cp_mgmt_domain_facts check_point.mgmt.cp_mgmt_domain_permissions_profile check_point.mgmt.cp_mgmt_domain_permissions_profile_facts check_point.mgmt.cp_mgmt_dynamic_global_network_object check_point.mgmt.cp_mgmt_dynamic_global_network_object_facts check_point.mgmt.cp_mgmt_dynamic_object check_point.mgmt.cp_mgmt_dynamic_object_facts check_point.mgmt.cp_mgmt_exception_group check_point.mgmt.cp_mgmt_exception_group_facts check_point.mgmt.cp_mgmt_export_management check_point.mgmt.cp_mgmt_export_smart_task check_point.mgmt.cp_mgmt_get_attachment check_point.mgmt.cp_mgmt_get_interfaces check_point.mgmt.cp_mgmt_get_platform check_point.mgmt.cp_mgmt_global_assignment check_point.mgmt.cp_mgmt_global_assignment_facts check_point.mgmt.cp_mgmt_group check_point.mgmt.cp_mgmt_group_facts check_point.mgmt.cp_mgmt_group_with_exclusion check_point.mgmt.cp_mgmt_group_with_exclusion_facts check_point.mgmt.cp_mgmt_gsn_handover_group check_point.mgmt.cp_mgmt_gsn_handover_group_facts check_point.mgmt.cp_mgmt_ha_full_sync check_point.mgmt.cp_mgmt_host check_point.mgmt.cp_mgmt_host_facts check_point.mgmt.cp_mgmt_hosts check_point.mgmt.cp_mgmt_https_layer check_point.mgmt.cp_mgmt_https_layer_facts check_point.mgmt.cp_mgmt_https_section check_point.mgmt.cp_mgmt_identity_tag check_point.mgmt.cp_mgmt_identity_tag_facts check_point.mgmt.cp_mgmt_idp_administrator_group check_point.mgmt.cp_mgmt_idp_administrator_group_facts check_point.mgmt.cp_mgmt_idp_to_domain_assignment_facts check_point.mgmt.cp_mgmt_import_management check_point.mgmt.cp_mgmt_import_smart_task check_point.mgmt.cp_mgmt_install_database check_point.mgmt.cp_mgmt_install_lsm_policy check_point.mgmt.cp_mgmt_install_lsm_settings check_point.mgmt.cp_mgmt_install_policy check_point.mgmt.cp_mgmt_install_software_package check_point.mgmt.cp_mgmt_interoperable_device check_point.mgmt.cp_mgmt_interoperable_device_facts check_point.mgmt.cp_mgmt_ips_protection_extended_attribute_facts check_point.mgmt.cp_mgmt_lock_object check_point.mgmt.cp_mgmt_lsm_cluster check_point.mgmt.cp_mgmt_lsm_cluster_facts check_point.mgmt.cp_mgmt_lsm_cluster_profile_facts check_point.mgmt.cp_mgmt_lsm_gateway check_point.mgmt.cp_mgmt_lsm_gateway_facts check_point.mgmt.cp_mgmt_lsm_gateway_profile_facts check_point.mgmt.cp_mgmt_lsm_run_script check_point.mgmt.cp_mgmt_lsv_profile check_point.mgmt.cp_mgmt_lsv_profile_facts check_point.mgmt.cp_mgmt_md_permissions_profile check_point.mgmt.cp_mgmt_md_permissions_profile_facts check_point.mgmt.cp_mgmt_mds check_point.mgmt.cp_mgmt_mds_facts check_point.mgmt.cp_mgmt_multicast_address_range check_point.mgmt.cp_mgmt_multicast_address_range_facts check_point.mgmt.cp_mgmt_nat_rule check_point.mgmt.cp_mgmt_nat_rule_facts check_point.mgmt.cp_mgmt_nat_section check_point.mgmt.cp_mgmt_network check_point.mgmt.cp_mgmt_network_facts check_point.mgmt.cp_mgmt_network_feed check_point.mgmt.cp_mgmt_network_feed_facts check_point.mgmt.cp_mgmt_objects_facts check_point.mgmt.cp_mgmt_package check_point.mgmt.cp_mgmt_package_facts check_point.mgmt.cp_mgmt_provisioning_profile_facts check_point.mgmt.cp_mgmt_publish check_point.mgmt.cp_mgmt_put_file check_point.mgmt.cp_mgmt_radius_group check_point.mgmt.cp_mgmt_radius_group_facts check_point.mgmt.cp_mgmt_radius_server check_point.mgmt.cp_mgmt_radius_server_facts check_point.mgmt.cp_mgmt_reject_session check_point.mgmt.cp_mgmt_repository_package_facts check_point.mgmt.cp_mgmt_repository_script check_point.mgmt.cp_mgmt_repository_script_facts check_point.mgmt.cp_mgmt_reset_sic check_point.mgmt.cp_mgmt_run_ips_update check_point.mgmt.cp_mgmt_run_script check_point.mgmt.cp_mgmt_security_zone check_point.mgmt.cp_mgmt_security_zone_facts check_point.mgmt.cp_mgmt_service_citrix_tcp check_point.mgmt.cp_mgmt_service_citrix_tcp_facts check_point.mgmt.cp_mgmt_service_compound_tcp check_point.mgmt.cp_mgmt_service_compound_tcp_facts check_point.mgmt.cp_mgmt_service_dce_rpc check_point.mgmt.cp_mgmt_service_dce_rpc_facts check_point.mgmt.cp_mgmt_service_group check_point.mgmt.cp_mgmt_service_group_facts check_point.mgmt.cp_mgmt_service_icmp check_point.mgmt.cp_mgmt_service_icmp6 check_point.mgmt.cp_mgmt_service_icmp6_facts check_point.mgmt.cp_mgmt_service_icmp_facts check_point.mgmt.cp_mgmt_service_other check_point.mgmt.cp_mgmt_service_other_facts check_point.mgmt.cp_mgmt_service_rpc check_point.mgmt.cp_mgmt_service_rpc_facts check_point.mgmt.cp_mgmt_service_sctp check_point.mgmt.cp_mgmt_service_sctp_facts check_point.mgmt.cp_mgmt_service_tcp check_point.mgmt.cp_mgmt_service_tcp_facts check_point.mgmt.cp_mgmt_service_udp check_point.mgmt.cp_mgmt_service_udp_facts check_point.mgmt.cp_mgmt_session_facts check_point.mgmt.cp_mgmt_set_api_settings check_point.mgmt.cp_mgmt_set_cloud_services check_point.mgmt.cp_mgmt_set_domain check_point.mgmt.cp_mgmt_set_global_domain check_point.mgmt.cp_mgmt_set_global_properties check_point.mgmt.cp_mgmt_set_ha_state check_point.mgmt.cp_mgmt_set_idp_default_assignment check_point.mgmt.cp_mgmt_set_idp_to_domain_assignment check_point.mgmt.cp_mgmt_set_ips_update_schedule check_point.mgmt.cp_mgmt_set_login_message check_point.mgmt.cp_mgmt_set_nat_rule check_point.mgmt.cp_mgmt_set_policy_settings check_point.mgmt.cp_mgmt_set_session check_point.mgmt.cp_mgmt_set_threat_advanced_settings check_point.mgmt.cp_mgmt_set_vpn_community_remote_access check_point.mgmt.cp_mgmt_show_access_section check_point.mgmt.cp_mgmt_show_api_settings check_point.mgmt.cp_mgmt_show_api_versions check_point.mgmt.cp_mgmt_show_azure_ad_content check_point.mgmt.cp_mgmt_show_changes check_point.mgmt.cp_mgmt_show_cloud_services check_point.mgmt.cp_mgmt_show_commands check_point.mgmt.cp_mgmt_show_gateways_and_servers check_point.mgmt.cp_mgmt_show_global_domain check_point.mgmt.cp_mgmt_show_global_properties check_point.mgmt.cp_mgmt_show_ha_state check_point.mgmt.cp_mgmt_show_https_section check_point.mgmt.cp_mgmt_show_idp_default_assignment check_point.mgmt.cp_mgmt_show_ips_status check_point.mgmt.cp_mgmt_show_ips_update_schedule check_point.mgmt.cp_mgmt_show_layer_structure check_point.mgmt.cp_mgmt_show_login_message check_point.mgmt.cp_mgmt_show_logs check_point.mgmt.cp_mgmt_show_nat_section check_point.mgmt.cp_mgmt_show_place_holder check_point.mgmt.cp_mgmt_show_policy_settings check_point.mgmt.cp_mgmt_show_servers_and_processes check_point.mgmt.cp_mgmt_show_software_package_details check_point.mgmt.cp_mgmt_show_software_packages_per_targets check_point.mgmt.cp_mgmt_show_task check_point.mgmt.cp_mgmt_show_tasks check_point.mgmt.cp_mgmt_show_threat_advanced_settings check_point.mgmt.cp_mgmt_show_unused_objects check_point.mgmt.cp_mgmt_show_updatable_objects_repository_content check_point.mgmt.cp_mgmt_show_validations check_point.mgmt.cp_mgmt_simple_cluster check_point.mgmt.cp_mgmt_simple_cluster_facts check_point.mgmt.cp_mgmt_simple_gateway check_point.mgmt.cp_mgmt_simple_gateway_facts check_point.mgmt.cp_mgmt_smart_task check_point.mgmt.cp_mgmt_smart_task_facts check_point.mgmt.cp_mgmt_smart_task_trigger_facts check_point.mgmt.cp_mgmt_smtp_server check_point.mgmt.cp_mgmt_smtp_server_facts check_point.mgmt.cp_mgmt_submit_session check_point.mgmt.cp_mgmt_tacacs_group check_point.mgmt.cp_mgmt_tacacs_group_facts check_point.mgmt.cp_mgmt_tacacs_server check_point.mgmt.cp_mgmt_tacacs_server_facts check_point.mgmt.cp_mgmt_tag check_point.mgmt.cp_mgmt_tag_facts check_point.mgmt.cp_mgmt_task_facts check_point.mgmt.cp_mgmt_test_sic_status check_point.mgmt.cp_mgmt_threat_exception check_point.mgmt.cp_mgmt_threat_exception_facts check_point.mgmt.cp_mgmt_threat_indicator check_point.mgmt.cp_mgmt_threat_indicator_facts check_point.mgmt.cp_mgmt_threat_layer check_point.mgmt.cp_mgmt_threat_layer_facts check_point.mgmt.cp_mgmt_threat_layers check_point.mgmt.cp_mgmt_threat_profile check_point.mgmt.cp_mgmt_threat_profile_facts check_point.mgmt.cp_mgmt_threat_protection_override check_point.mgmt.cp_mgmt_threat_rule check_point.mgmt.cp_mgmt_threat_rule_facts check_point.mgmt.cp_mgmt_time check_point.mgmt.cp_mgmt_time_facts check_point.mgmt.cp_mgmt_time_group check_point.mgmt.cp_mgmt_time_group_facts check_point.mgmt.cp_mgmt_trusted_client check_point.mgmt.cp_mgmt_trusted_client_facts check_point.mgmt.cp_mgmt_uninstall_software_package check_point.mgmt.cp_mgmt_unlock_administrator check_point.mgmt.cp_mgmt_unlock_object check_point.mgmt.cp_mgmt_updatable_object_facts check_point.mgmt.cp_mgmt_update_provisioned_satellites check_point.mgmt.cp_mgmt_update_updatable_objects_repository_content check_point.mgmt.cp_mgmt_user_group check_point.mgmt.cp_mgmt_user_group_facts check_point.mgmt.cp_mgmt_verify_policy check_point.mgmt.cp_mgmt_verify_software_package check_point.mgmt.cp_mgmt_vpn_community_meshed check_point.mgmt.cp_mgmt_vpn_community_meshed_facts check_point.mgmt.cp_mgmt_vpn_community_remote_access_facts check_point.mgmt.cp_mgmt_vpn_community_star check_point.mgmt.cp_mgmt_vpn_community_star_facts check_point.mgmt.cp_mgmt_vsx_run_operation check_point.mgmt.cp_mgmt_where_used check_point.mgmt.cp_mgmt_wildcard check_point.mgmt.cp_mgmt_wildcard_facts" returned exit status 1.
>>> Standard Error
ERROR! Unable to retrieve documentation from 'check_point.mgmt.cp_mgmt_lock_object' due to: sequence item 1: expected str instance, AnsibleMapping found. sequence item 1: expected str instance, AnsibleMapping found
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 240 errors:

``` text
plugins/modules/cp_mgmt_abort_get_interfaces.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_abort_get_interfaces.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_access_layer.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_access_layer.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_access_layers', 'why': 'Newer and updated modules released with more functionality.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_access_point_name_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_add_api_key.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_add_api_key.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_add_data_center_object.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_add_data_center_object.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_add_domain.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_add_domain.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_add_nat_rule.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_add_nat_rule.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_nat_rule', 'why': 'Newer and updated module released with more functionality.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_add_nat_rule.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_add_nat_rule.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_add_repository_package.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_add_repository_package.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_add_updatable_object.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_add_updatable_object.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_approve_session.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_approve_session.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_assign_global_assignment.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_assign_global_assignment.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_checkpoint_host_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_connect_cloud_services.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_connect_cloud_services.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_delete_api_key.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_delete_api_key.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_delete_data_center_object.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_delete_data_center_object.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_delete_domain.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_delete_domain.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_delete_nat_rule.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_delete_nat_rule.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_nat_rule', 'why': 'Newer and updated module released with more functionality.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_delete_nat_rule.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_delete_nat_rule.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_delete_repository_package.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_delete_repository_package.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_delete_updatable_object.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_delete_updatable_object.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_discard.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_discard.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_disconnect_cloud_services.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_disconnect_cloud_services.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_dynamic_global_network_object_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_export_management.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_export_management.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_export_smart_task.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_export_smart_task.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_get_attachment.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_get_attachment.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_get_interfaces.py:0:0: invalid-documentation: DOCUMENTATION.Note: extra keys not allowed @ data['Note']. Got 'The fetched topology is based on static routes.'
plugins/modules/cp_mgmt_get_interfaces.py:0:0: invalid-documentation: DOCUMENTATION.Prerequisites: extra keys not allowed @ data['Prerequisites']. Got ['SIC must be established in the Security Gateway or Cluster Member object.', 'Security Gateway or Cluster Members must be up and running. - All operations are performed over Web Services API.']
plugins/modules/cp_mgmt_get_interfaces.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_get_interfaces.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_gsn_handover_group_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_ha_full_sync.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_ha_full_sync.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_host.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_host.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_hosts', 'why': 'Newer and updated modules released with more functionality.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_hosts.py:0:0: invalid-documentation: DOCUMENTATION.author: Invalid author for dictionary value @ data['author']. Got 'Ansible Team'
plugins/modules/cp_mgmt_https_layer_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_import_management.py:0:0: doc-required-mismatch: Argument 'file_path' in argument_spec is not required, but is documented as being required
plugins/modules/cp_mgmt_import_management.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_import_management.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_import_smart_task.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_import_smart_task.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_install_database.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_install_database.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_install_lsm_policy.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_install_lsm_policy.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_install_lsm_settings.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_install_lsm_settings.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_install_policy.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_install_policy.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_install_software_package.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_install_software_package.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_ips_protection_extended_attribute_facts.py:0:0: doc-elements-mismatch: Argument 'order' in argument_spec does not specify elements,but elements is documented as being dict
plugins/modules/cp_mgmt_ips_protection_extended_attribute_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.argument_spec.order.elememnts: extra keys not allowed @ data['argument_spec']['order']['elememnts']. Got 'dict'
plugins/modules/cp_mgmt_ips_protection_extended_attribute_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_ips_protection_extended_attribute_facts.py:0:0: parameter-list-no-elements: Argument 'order' in argument_spec defines type as list but elements is not defined
plugins/modules/cp_mgmt_lock_object.py:0:0: invalid-documentation: DOCUMENTATION.description.1: Must be a string @ data['description'][1]. Got {'The object can be unlocked by the following commands': 'unlock, publish or discard.'}
plugins/modules/cp_mgmt_lock_object.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_lock_object.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_lsm_run_script.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_lsm_run_script.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_lsv_profile.py:0:0: doc-choices-incompatible-type: Argument 'max_allowed_addresses' in documentation found in vpn_domain defines choices as ('1-256') but this is incompatible with argument type 'int'
plugins/modules/cp_mgmt_lsv_profile.py:0:0: doc-choices-incompatible-type: DOCUMENTATION.options.vpn_domain.suboptions.max_allowed_addresses: Argument defines choices as ('1-256') but this is incompatible with argument type int: invalid literal for int() with base 10: '1-256' for dictionary value @ data['options']['vpn_domain']['suboptions']['max_allowed_addresses']. Got {'description': ['Maximum number of IP addresses in the VPN Domain of each peer. This value will be enforced only when limit-peer-domain-size field is set to true. Select a value between 1 and 256. Default value is 256.'], 'type': 'int', 'choices': ['1-256']}
plugins/modules/cp_mgmt_lsv_profile_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_publish.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_publish.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_put_file.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_put_file.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_radius_group_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_radius_server_facts.py:0:0: doc-elements-mismatch: Argument 'domains_to_process' in argument_spec specifies elements as str,but elements is not documented
plugins/modules/cp_mgmt_radius_server_facts.py:0:0: doc-elements-mismatch: Argument 'order' in argument_spec specifies elements as dict,but elements is not documented
plugins/modules/cp_mgmt_radius_server_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_radius_server_facts.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.domains_to_process: Argument defines type as list but elements is not defined for dictionary value @ data['options']['domains_to_process']. Got {'description': ['Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.'], 'type': 'list'}
plugins/modules/cp_mgmt_radius_server_facts.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.order: Argument defines type as list but elements is not defined for dictionary value @ data['options']['order']. Got {'description': ['Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order. This parameter is relevant only for getting few objects.'], 'type': 'list', 'suboptions': {'ASC': {'description': ['Sorts results by the given field in ascending order.'], 'type': 'str', 'choices': ['name']}, 'DESC': {'description': ['Sorts results by the given field in descending order.'], 'type': 'str', 'choices': ['name']}}}
plugins/modules/cp_mgmt_reject_session.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_reject_session.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_repository_package_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_run_ips_update.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_run_ips_update.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_run_script.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_run_script.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_service_citrix_tcp_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_service_compound_tcp_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_set_api_settings.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_api_settings.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_cloud_services.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_cloud_services.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_domain.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_domain.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_global_domain.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_global_domain.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_ha_state.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_ha_state.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_ips_update_schedule.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_ips_update_schedule.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_login_message.py:0:0: invalid-argument-name: Argument 'message' in argument_spec must not be one of message,syslog_facility as it is used internally by Ansible Core Engine
plugins/modules/cp_mgmt_set_login_message.py:0:0: nonexistent-parameter-documented: Argument 'message' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/cp_mgmt_set_login_message.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_login_message.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_nat_rule.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_set_nat_rule.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_nat_rule', 'why': 'Newer and updated module released with more functionality.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_set_nat_rule.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_nat_rule.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_policy_settings.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_policy_settings.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_session.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_session.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_set_vpn_community_remote_access.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_set_vpn_community_remote_access.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_access_section.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_access_section.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_api_settings.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_api_settings.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_api_versions.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_api_versions.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_azure_ad_content.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_azure_ad_content.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_changes.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_changes.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_cloud_services.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_cloud_services.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_commands.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_commands.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_gateways_and_servers.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_gateways_and_servers.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_global_domain.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_global_domain.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_global_properties.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_global_properties.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_ha_state.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_ha_state.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_https_section.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_https_section.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_idp_default_assignment.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_idp_default_assignment.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_ips_status.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_ips_status.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_ips_update_schedule.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_ips_update_schedule.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_layer_structure.py:0:0: invalid-documentation: DOCUMENTATION.description.1: Must be a string @ data['description'][1]. Got {'Supported layer types': 'Access Control, NAT, Custom Threat Prevention, Threat Exception and HTTPS Inspection.'}
plugins/modules/cp_mgmt_show_layer_structure.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_layer_structure.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_login_message.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_login_message.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_logs.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_logs.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_nat_section.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_nat_section.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_place_holder.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_place_holder.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_policy_settings.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_policy_settings.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_servers_and_processes.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_servers_and_processes.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_software_package_details.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_software_package_details.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_software_packages_per_targets.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_software_packages_per_targets.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_task.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_show_task.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_task_facts', 'why': 'Newer single facts module released.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_show_task.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_task.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_tasks.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_show_tasks.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_task_facts', 'why': 'Newer single facts module released.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_show_tasks.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_tasks.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_threat_advanced_settings.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_threat_advanced_settings.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_unused_objects.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_unused_objects.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_updatable_objects_repository_content.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_updatable_objects_repository_content.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_show_validations.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_show_validations.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_smart_task.py:0:0: no-log-needed: Argument 'shared_secret' in argument_spec could be a secret, though doesn't have `no_log` set found in action -> send_web_request
plugins/modules/cp_mgmt_smart_task_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_smart_task_trigger_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_submit_session.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_submit_session.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_tacacs_group_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_tacacs_server_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_task_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_test_sic_status.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_test_sic_status.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_threat_layer.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/cp_mgmt_threat_layer.py:0:0: invalid-documentation: DOCUMENTATION.deprecated: extra keys not allowed @ data['deprecated']. Got {'alternative': 'cp_mgmt_threat_layers', 'why': 'Newer and updated modules released with more functionality.', 'removed_at_date': '2024-11-01', 'removed_from_collection': 'check_point.mgmt'}
plugins/modules/cp_mgmt_threat_layers.py:0:0: invalid-documentation: DOCUMENTATION.author: Invalid author for dictionary value @ data['author']. Got 'Ansible Team'
plugins/modules/cp_mgmt_threat_protection_override.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_threat_protection_override.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_time_group_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_uninstall_software_package.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_uninstall_software_package.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_unlock_administrator.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_unlock_administrator.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_unlock_object.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_unlock_object.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_updatable_object_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_update_provisioned_satellites.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_update_provisioned_satellites.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_update_updatable_objects_repository_content.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_update_updatable_objects_repository_content.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_user_group_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_verify_policy.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_verify_policy.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_verify_software_package.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_verify_software_package.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_vpn_community_remote_access_facts.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/cp_mgmt_vpn_community_star.py:0:0: no-log-needed: Argument 'ike_p1_rekey_time' in argument_spec could be a secret, though doesn't have `no_log` set found in granular_encryptions -> ike_phase_1
plugins/modules/cp_mgmt_vpn_community_star.py:0:0: no-log-needed: Argument 'ike_p1_rekey_time' in argument_spec could be a secret, though doesn't have `no_log` set found in ike_phase_1
plugins/modules/cp_mgmt_vpn_community_star.py:0:0: no-log-needed: Argument 'ike_p2_rekey_time' in argument_spec could be a secret, though doesn't have `no_log` set found in granular_encryptions -> ike_phase_2
plugins/modules/cp_mgmt_vpn_community_star.py:0:0: no-log-needed: Argument 'ike_p2_rekey_time' in argument_spec could be a secret, though doesn't have `no_log` set found in ike_phase_2
plugins/modules/cp_mgmt_vsx_run_operation.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_vsx_run_operation.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/cp_mgmt_where_used.py:0:0: parameter-type-not-in-doc: Argument 'auto_publish_session' in argument_spec defines type as 'bool' but documentation doesn't define type
plugins/modules/cp_mgmt_where_used.py:0:0: undocumented-parameter: Argument 'auto_publish_session' is listed in the argument_spec, but not documented in the module documentation
```



## File divergences

The following files differ between the `v5.1.1` git tag and `check_point-mgmt-5.1.1.tar.gz` on Ansible Galaxy:

- `tests/units/plugins/httpapi/test_checkpoint.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_wildcard.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_administrator_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_publish.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_global_assignment.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_dns_domain.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_assign_global_assignment.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_application_site_group.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_host_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_verify_software_package.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_security_zone_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_uninstall_software_package.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_group_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_application_site_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_checkpoint_host.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_profile_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_application_site.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_layer.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_icmp_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_vpn_community_star.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_indicator.py` (`WRONG_HASH`)
- `tests/units/modules/test_checkpoint_task_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_udp.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_session_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_icmp6.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_role_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_add_data_center_object.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_show_https_section.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_simple_gateway_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_sctp_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_rule_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_group.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_host.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_layer_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_mds_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_application_site_group_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_rpc.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_network.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_vpn_community_meshed_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_discard.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_network_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_dce_rpc.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_delete_nat_rule.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_nat_section.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_simple_gateway.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_udp_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_icmp.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_exception_group.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_https_section.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_global_assignment_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_delete_api_key.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_time.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_multicast_address_range_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_other_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_checkpoint_access_rule.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_time_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_run_script.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_exception.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_delete_data_center_object.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_role.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_other.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_rpc_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_vpn_community_meshed.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_group_with_exclusion.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_group_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_group_with_exclusion_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_set_nat_rule.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_vpn_community_star_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_show_access_section.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_icmp6_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_layer_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_show_nat_section.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_dce_rpc_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_show_software_package_details.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_section.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_address_range.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_add_nat_rule.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_tag.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_put_file.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_dns_domain_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_indicator_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_address_range_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_tcp_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_exception_group_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_package.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_rule.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_data_center_object_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_dynamic_object_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_security_zone.py` (`WRONG_HASH`)
- `tests/units/modules/test_checkpoint_session.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_multicast_address_range.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_tag_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_profile.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_wildcard_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_application_site_category.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_administrator.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_package_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_application_site_category_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_layer.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_install_policy.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_rule.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_run_ips_update.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_protection_override.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_access_rule_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_tcp.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_threat_exception_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_dynamic_object.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_verify_policy.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_install_software_package.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_add_api_key.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_nat_rule_facts.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_service_sctp.py` (`WRONG_HASH`)
- `tests/units/modules/test_cp_mgmt_group.py` (`WRONG_HASH`)
- `plugins/action/cp_mgmt_hosts.py` (`WRONG_HASH`)
- `plugins/action/cp_mgmt_access_rules.py` (`WRONG_HASH`)
- `plugins/doc_fragments/checkpoint_commands.py` (`WRONG_HASH`)
- `plugins/doc_fragments/checkpoint_objects_action_module.py` (`WRONG_HASH`)
- `plugins/doc_fragments/checkpoint_objects.py` (`WRONG_HASH`)
- `plugins/doc_fragments/checkpoint_facts.py` (`WRONG_HASH`)
- `plugins/httpapi/checkpoint.py` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
