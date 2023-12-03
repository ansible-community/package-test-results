# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.0.5` of `wti.remote`, corresponding to the `v1.0.5` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test ansible-doc` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/ansible-doc.html)] failed with the error:

``` text
Output on stderr from ansible-doc is considered an error.

Command "ansible-doc -t lookup wti.remote.cpm_alarm_info wti.remote.cpm_config_backup wti.remote.cpm_config_restore wti.remote.cpm_current_info wti.remote.cpm_firmware_info wti.remote.cpm_firmware_update wti.remote.cpm_hostname_config wti.remote.cpm_hostname_info wti.remote.cpm_interface_config wti.remote.cpm_interface_info wti.remote.cpm_iptables_config wti.remote.cpm_iptables_info wti.remote.cpm_metering wti.remote.cpm_plugconfig wti.remote.cpm_plugcontrol wti.remote.cpm_power_info wti.remote.cpm_serial_port_action_info wti.remote.cpm_serial_port_action_set wti.remote.cpm_serial_port_config wti.remote.cpm_serial_port_info wti.remote.cpm_snmp_config wti.remote.cpm_snmp_info wti.remote.cpm_status wti.remote.cpm_status_info wti.remote.cpm_syslog_client_config wti.remote.cpm_syslog_client_info wti.remote.cpm_syslog_server_config wti.remote.cpm_syslog_server_info wti.remote.cpm_temp_info wti.remote.cpm_time_config wti.remote.cpm_time_info wti.remote.cpm_user" returned exit status 0.
>>> Standard Error
[WARNING]: While constructing a mapping from
/root/ansible_collections/wti/remote/plugins/lookup/cpm_snmp_config.py, line
58, column 9, found a duplicate dict key (type). Using last defined value only.
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 85 errors:

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

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/yamllint.html)] failed with 4 errors:

``` text
meta/runtime.yml:35:1: empty-lines: too many blank lines (1 > 0)
playbooks/cpm_syslog_client/syslog_client_info.yml:30:1: empty-lines: too many blank lines (1 > 0)
playbooks/cpm_syslog_server/syslog_server_config.yml:40:1: empty-lines: too many blank lines (1 > 0)
playbooks/cpm_syslog_server/syslog_server_info.yml:30:1: empty-lines: too many blank lines (1 > 0)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
