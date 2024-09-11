# Community package requirements: sanity tests and repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.0.8` of `wti.remote`, corresponding to the `v1.0.8` tag in this repo, fails one or more of the required sanity tests.

The contents in the `v1.0.8` git tag do not match `wti-remote-1.0.8.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.17.4`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.17/dev_guide/testing/sanity/validate-modules.html)] failed with 85 errors:

``` text
plugins/lookup/cpm_alarm_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_alarm_info'
plugins/lookup/cpm_alarm_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_alarm_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_config_backup.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_config_backup'
plugins/lookup/cpm_config_backup.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_config_backup.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_config_restore.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_config_restore'
plugins/lookup/cpm_config_restore.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_config_restore.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_current_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_current_info'
plugins/lookup/cpm_current_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_current_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_firmware_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_firmware_info'
plugins/lookup/cpm_firmware_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_firmware_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_firmware_update.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_firmware_update'
plugins/lookup/cpm_firmware_update.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_firmware_update.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_hostname_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_hostname_config'
plugins/lookup/cpm_hostname_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_hostname_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_hostname_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_hostname_info'
plugins/lookup/cpm_hostname_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_hostname_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_interface_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_interface_config'
plugins/lookup/cpm_interface_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_interface_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_interface_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_interface_info'
plugins/lookup/cpm_interface_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_interface_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_iptables_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_iptables_config'
plugins/lookup/cpm_iptables_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_iptables_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_iptables_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_iptables_info'
plugins/lookup/cpm_iptables_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_iptables_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_plugconfig.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_plugconfig'
plugins/lookup/cpm_plugconfig.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_plugcontrol.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_plugcontrol'
plugins/lookup/cpm_plugcontrol.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_power_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_power_info'
plugins/lookup/cpm_power_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_power_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_serial_port_action_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_serial_port_action_info'
plugins/lookup/cpm_serial_port_action_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_serial_port_action_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_serial_port_action_set.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_serial_port_action_set'
plugins/lookup/cpm_serial_port_action_set.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_serial_port_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_serial_port_config'
plugins/lookup/cpm_serial_port_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_serial_port_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_serial_port_info'
plugins/lookup/cpm_serial_port_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_serial_port_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_snmp_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_snmp_config'
plugins/lookup/cpm_snmp_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_snmp_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_snmp_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_snmp_info'
plugins/lookup/cpm_snmp_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_snmp_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_status_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_status_info'
plugins/lookup/cpm_status_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_status_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_syslog_client_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_syslog_client_config'
plugins/lookup/cpm_syslog_client_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_syslog_client_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_syslog_client_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_syslog_client_info'
plugins/lookup/cpm_syslog_client_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_syslog_client_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_syslog_server_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_syslog_server_config'
plugins/lookup/cpm_syslog_server_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_syslog_server_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_syslog_server_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_syslog_server_info'
plugins/lookup/cpm_syslog_server_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_syslog_server_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_temp_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_temp_info'
plugins/lookup/cpm_temp_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_temp_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_time_config.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_time_config'
plugins/lookup/cpm_time_config.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_time_config.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_time_info.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_time_info'
plugins/lookup/cpm_time_info.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/lookup/cpm_time_info.py:0:0: return-syntax-error: RETURN.data.type: not a valid value for dictionary value @ data['data']['type']. Got 'complex'
plugins/lookup/cpm_user.py:0:0: invalid-documentation: DOCUMENTATION.module: extra keys not allowed @ data['module']. Got 'cpm_user'
plugins/lookup/cpm_user.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
```



## File divergences

The following files differ between the `v1.0.8` git tag and `wti-remote-1.0.8.tar.gz` on Ansible Galaxy:

- `docs/cpm_syslog_client_config.rst` (`WRONG_HASH`)
- `docs/cpm_hostname_config.rst` (`WRONG_HASH`)
- `docs/cpm_syslog_server_config.rst` (`WRONG_HASH`)
- `docs/cpm_snmp_config.rst` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
