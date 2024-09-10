# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.3.0` of `google.cloud`, corresponding to the `v1.3.0` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.17.3`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.17/dev_guide/testing/sanity/validate-modules.html)] failed with 186 errors:

``` text
plugins/inventory/gcp_compute.py:0:0: invalid-documentation: DOCUMENTATION.plugin_type: extra keys not allowed @ data['plugin_type']. Got 'inventory'
plugins/inventory/gcp_compute.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.filters: Argument defines type as list but elements is not defined for dictionary value @ data['options']['filters']. Got {'description': 'A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList). Each additional filter in the list will be added as an AND condition (filter1 and filter2)\n', 'type': 'list'}
plugins/inventory/gcp_compute.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.folders: Argument defines type as list but elements is not defined for dictionary value @ data['options']['folders']. Got {'description': 'A folder that contains many projects', 'type': 'list', 'required': False}
plugins/inventory/gcp_compute.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.hostnames: Argument defines type as list but elements is not defined for dictionary value @ data['options']['hostnames']. Got {'description': "A list of options that describe the ordering for which hostnames should be assigned. Currently supported hostnames are 'public_ip', 'private_ip', 'name' or 'labels.vm_name'.", 'default': ['public_ip', 'private_ip', 'name'], 'type': 'list'}
plugins/inventory/gcp_compute.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.projects: Argument defines type as list but elements is not defined for dictionary value @ data['options']['projects']. Got {'description': 'A list of projects in which to describe GCE instances.', 'type': 'list', 'required': False}
plugins/inventory/gcp_compute.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.scopes: Argument defines type as list but elements is not defined for dictionary value @ data['options']['scopes']. Got {'description': 'list of authentication scopes', 'type': 'list', 'default': ['https://www.googleapis.com/auth/compute'], 'env': [{'name': 'GCP_SCOPES'}]}
plugins/inventory/gcp_compute.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.zones: Argument defines type as list but elements is not defined for dictionary value @ data['options']['zones']. Got {'description': 'A list of regions in which to describe GCE instances. If none provided, it defaults to all zones available to a given project.', 'type': 'list'}
plugins/modules/gcp_appengine_firewall_rule_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_bigquery_dataset_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_bigquery_table.py:0:0: doc-default-does-not-match-spec: Argument 'max_bad_records' in argument_spec found in external_data_configuration defines default as (0) but documentation defines default as (None)
plugins/modules/gcp_bigquery_table.py:0:0: doc-default-does-not-match-spec: Argument 'skip_leading_rows' in argument_spec found in external_data_configuration -> csv_options defines default as (0) but documentation defines default as (None)
plugins/modules/gcp_bigquery_table.py:0:0: doc-default-does-not-match-spec: Argument 'skip_leading_rows' in argument_spec found in external_data_configuration -> google_sheets_options defines default as (0) but documentation defines default as (None)
plugins/modules/gcp_bigquery_table_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_bigtable_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_cloudbuild_trigger.py:0:0: no-log-needed: Argument 'secret' in argument_spec could be a secret, though doesn't have `no_log` set found in webhook_config
plugins/modules/gcp_cloudbuild_trigger.py:0:0: no-log-needed: Argument 'secret_env' in argument_spec could be a secret, though doesn't have `no_log` set found in build -> options
plugins/modules/gcp_cloudbuild_trigger.py:0:0: no-log-needed: Argument 'secret_env' in argument_spec could be a secret, though doesn't have `no_log` set found in build -> secrets
plugins/modules/gcp_cloudbuild_trigger.py:0:0: no-log-needed: Argument 'secret_env' in argument_spec could be a secret, though doesn't have `no_log` set found in build -> steps
plugins/modules/gcp_cloudbuild_trigger.py:0:0: no-log-needed: Argument 'secrets' in argument_spec could be a secret, though doesn't have `no_log` set found in build
plugins/modules/gcp_cloudbuild_trigger_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_cloudfunctions_cloud_function_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_cloudscheduler_job.py:0:0: no-log-needed: Argument 'oauth_token' in argument_spec could be a secret, though doesn't have `no_log` set found in http_target
plugins/modules/gcp_cloudscheduler_job.py:0:0: no-log-needed: Argument 'oidc_token' in argument_spec could be a secret, though doesn't have `no_log` set found in http_target
plugins/modules/gcp_cloudscheduler_job_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_cloudtasks_queue_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_address_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_autoscaler_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_backend_bucket_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_backend_service.py:0:0: doc-default-does-not-match-spec: Argument 'capacity_scaler' in argument_spec found in backends defines default as ('1') but documentation defines default as ('1.0')
plugins/modules/gcp_compute_backend_service.py:0:0: doc-default-does-not-match-spec: Argument 'enforcing_consecutive_gateway_failure' in argument_spec found in outlier_detection defines default as (0) but documentation defines default as (None)
plugins/modules/gcp_compute_backend_service.py:0:0: invalid-documentation-markup: Directive "O(1)" contains a non-existing option "1"
plugins/modules/gcp_compute_backend_service.py:0:0: no-log-needed: Argument 'cache_key_policy' in argument_spec could be a secret, though doesn't have `no_log` set found in cdn_policy
plugins/modules/gcp_compute_backend_service.py:0:0: parameter-type-not-in-doc: Argument 'fingerprint' in argument_spec defines type as 'str' but documentation doesn't define type
plugins/modules/gcp_compute_backend_service.py:0:0: undocumented-parameter: Argument 'fingerprint' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/gcp_compute_backend_service_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_backend_service_info.py:0:0: invalid-documentation-markup: Directive "O(1)" contains a non-existing option "1"
plugins/modules/gcp_compute_disk.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disk_encryption_key
plugins/modules/gcp_compute_disk.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in source_image_encryption_key
plugins/modules/gcp_compute_disk.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in source_snapshot_encryption_key
plugins/modules/gcp_compute_disk_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_external_vpn_gateway_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_firewall_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_forwarding_rule_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_global_address_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_global_forwarding_rule_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_health_check.py:0:0: doc-default-does-not-match-spec: Argument 'enable' in argument_spec found in log_config defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_health_check_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_http_health_check_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_https_health_check_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_image.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in image_encryption_key
plugins/modules/gcp_compute_image.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in source_disk_encryption_key
plugins/modules/gcp_compute_image_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_instance.py:0:0: no-log-needed: Argument 'disk_encryption_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disks
plugins/modules/gcp_compute_instance.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disks -> disk_encryption_key
plugins/modules/gcp_compute_instance.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disks -> initialize_params -> source_image_encryption_key
plugins/modules/gcp_compute_instance.py:0:0: no-log-needed: Argument 'rsa_encrypted_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disks -> disk_encryption_key
plugins/modules/gcp_compute_instance.py:0:0: no-log-needed: Argument 'source_image_encryption_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disks -> initialize_params
plugins/modules/gcp_compute_instance_group_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_instance_group_manager_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_instance_template.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in properties -> disks -> disk_encryption_key
plugins/modules/gcp_compute_instance_template.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in properties -> disks -> initialize_params -> source_image_encryption_key
plugins/modules/gcp_compute_instance_template.py:0:0: no-log-needed: Argument 'rsa_encrypted_key' in argument_spec could be a secret, though doesn't have `no_log` set found in properties -> disks -> disk_encryption_key
plugins/modules/gcp_compute_instance_template_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_interconnect_attachment_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_network_endpoint_group_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_network_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_node_group_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_node_template_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_autoscaler_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_backend_service.py:0:0: doc-default-does-not-match-spec: Argument 'enforcing_consecutive_gateway_failure' in argument_spec found in outlier_detection defines default as (0) but documentation defines default as (None)
plugins/modules/gcp_compute_region_backend_service.py:0:0: invalid-documentation-markup: Directive "O(1)" contains a non-existing option "1"
plugins/modules/gcp_compute_region_backend_service.py:0:0: no-log-needed: Argument 'cache_key_policy' in argument_spec could be a secret, though doesn't have `no_log` set found in cdn_policy
plugins/modules/gcp_compute_region_backend_service_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_backend_service_info.py:0:0: invalid-documentation-markup: Directive "O(1)" contains a non-existing option "1"
plugins/modules/gcp_compute_region_disk.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in disk_encryption_key
plugins/modules/gcp_compute_region_disk.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in source_snapshot_encryption_key
plugins/modules/gcp_compute_region_disk_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_health_check.py:0:0: doc-default-does-not-match-spec: Argument 'enable' in argument_spec found in log_config defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_health_check_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_instance_group_manager_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_target_http_proxy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_target_https_proxy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'allow_credentials' in argument_spec found in path_matchers -> path_rules -> route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'allow_credentials' in argument_spec found in path_matchers -> route_rules -> route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'disabled' in argument_spec found in path_matchers -> route_rules -> route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in path_matchers -> default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in path_matchers -> path_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in path_matchers -> route_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'ignore_case' in argument_spec found in path_matchers -> route_rules -> match_rules defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'invert_match' in argument_spec found in path_matchers -> route_rules -> match_rules -> header_matches defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in path_matchers -> default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in path_matchers -> path_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in path_matchers -> route_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_region_url_map_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_reservation.py:0:0: doc-default-does-not-match-spec: Argument 'specific_reservation_required' in argument_spec defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_reservation_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_resource_policy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_route_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_router_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_snapshot.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in snapshot_encryption_key
plugins/modules/gcp_compute_snapshot.py:0:0: no-log-needed: Argument 'raw_key' in argument_spec could be a secret, though doesn't have `no_log` set found in source_disk_encryption_key
plugins/modules/gcp_compute_snapshot_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_ssl_certificate_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_ssl_policy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_subnetwork_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_http_proxy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_https_proxy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_pool_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_ssl_proxy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_tcp_proxy_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_target_vpn_gateway_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'allow_credentials' in argument_spec found in default_route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'allow_credentials' in argument_spec found in path_matchers -> default_route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'allow_credentials' in argument_spec found in path_matchers -> path_rules -> route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'allow_credentials' in argument_spec found in path_matchers -> route_rules -> route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'disabled' in argument_spec found in default_route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'disabled' in argument_spec found in path_matchers -> default_route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'disabled' in argument_spec found in path_matchers -> route_rules -> route_action -> cors_policy defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in path_matchers -> default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in path_matchers -> path_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'https_redirect' in argument_spec found in path_matchers -> route_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'ignore_case' in argument_spec found in path_matchers -> route_rules -> match_rules defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'invert_match' in argument_spec found in path_matchers -> route_rules -> match_rules -> header_matches defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'replace' in argument_spec found in default_route_action -> weighted_backend_services -> header_action -> request_headers_to_add defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'replace' in argument_spec found in default_route_action -> weighted_backend_services -> header_action -> response_headers_to_add defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'replace' in argument_spec found in path_matchers -> default_route_action -> weighted_backend_services -> header_action -> request_headers_to_add defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'replace' in argument_spec found in path_matchers -> default_route_action -> weighted_backend_services -> header_action -> response_headers_to_add defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in path_matchers -> default_url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in path_matchers -> path_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: doc-default-does-not-match-spec: Argument 'strip_query' in argument_spec found in path_matchers -> route_rules -> url_redirect defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_compute_url_map.py:0:0: parameter-type-not-in-doc: Argument 'fingerprint' in argument_spec defines type as 'str' but documentation doesn't define type
plugins/modules/gcp_compute_url_map.py:0:0: undocumented-parameter: Argument 'fingerprint' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/gcp_compute_url_map_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_compute_vpn_tunnel_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_container_cluster.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in node_config -> taints
plugins/modules/gcp_container_cluster.py:0:0: no-log-needed: Argument 'password' in argument_spec could be a secret, though doesn't have `no_log` set found in master_auth
plugins/modules/gcp_container_cluster_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_container_node_pool.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in config -> taints
plugins/modules/gcp_container_node_pool_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_dns_managed_zone.py:0:0: no-log-needed: Argument 'default_key_specs' in argument_spec could be a secret, though doesn't have `no_log` set found in dnssec_config
plugins/modules/gcp_dns_managed_zone.py:0:0: no-log-needed: Argument 'key_length' in argument_spec could be a secret, though doesn't have `no_log` set found in dnssec_config -> default_key_specs
plugins/modules/gcp_dns_managed_zone_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_dns_resource_record_set_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_filestore_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_iam_role_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_iam_service_account_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_kms_crypto_key.py:0:0: doc-default-does-not-match-spec: Argument 'skip_initial_version_creation' in argument_spec defines default as (False) but documentation defines default as (None)
plugins/modules/gcp_kms_crypto_key.py:0:0: no-log-needed: Argument 'key_ring' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/gcp_kms_crypto_key_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_kms_crypto_key_info.py:0:0: no-log-needed: Argument 'key_ring' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/gcp_kms_key_ring_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_logging_metric.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set found in metric_descriptor -> labels
plugins/modules/gcp_logging_metric_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_mlengine_model_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_mlengine_version_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_pubsub_subscription.py:0:0: no-log-needed: Argument 'oidc_token' in argument_spec could be a secret, though doesn't have `no_log` set found in push_config
plugins/modules/gcp_pubsub_subscription_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_pubsub_topic_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_redis_instance.py:0:0: doc-default-does-not-match-spec: Argument 'auth_enabled' in argument_spec defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_redis_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_resourcemanager_project_info.py:0:0: doc-type-does-not-match-spec: Argument 'page_size' in argument_spec defines type as 'int' but documentation defines type as 'str'
plugins/modules/gcp_resourcemanager_project_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_runtimeconfig_config_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_runtimeconfig_variable_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_serviceusage_service_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_sourcerepo_repository_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_spanner_database_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_spanner_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_sql_database_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_sql_instance.py:0:0: no-log-needed: Argument 'client_key' in argument_spec could be a secret, though doesn't have `no_log` set found in replica_configuration -> mysql_replica_configuration
plugins/modules/gcp_sql_instance.py:0:0: no-log-needed: Argument 'password' in argument_spec could be a secret, though doesn't have `no_log` set found in replica_configuration -> mysql_replica_configuration
plugins/modules/gcp_sql_instance_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_sql_ssl_cert.py:0:0: no-log-needed: Argument 'private_key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/gcp_sql_user.py:0:0: no-log-needed: Argument 'password' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/gcp_sql_user_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
plugins/modules/gcp_storage_default_object_acl.py:0:0: parameter-type-not-in-doc: Argument 'object' in argument_spec defines type as 'str' but documentation doesn't define type
plugins/modules/gcp_storage_default_object_acl.py:0:0: undocumented-parameter: Argument 'object' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/gcp_storage_object.py:0:0: doc-required-mismatch: Argument 'src' in argument_spec is not required, but is documented as being required
plugins/modules/gcp_tpu_node.py:0:0: doc-default-does-not-match-spec: Argument 'use_service_networking' in argument_spec defines default as (None) but documentation defines default as (False)
plugins/modules/gcp_tpu_node_info.py:0:0: invalid-ansiblemodule-schema: AnsibleModule.supports_check_mode: required key not provided @ data['supports_check_mode']. Got None
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
