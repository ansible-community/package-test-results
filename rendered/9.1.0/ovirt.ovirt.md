# Community package requirements: sanity tests and repository management

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `3.2.0` of `ovirt.ovirt`, corresponding to the `3.2.0-1` tag in this repo, fails one or more of the required sanity tests.

The contents in the `3.2.0-1` git tag do not match `ovirt-ovirt-3.2.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

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
Output on stderr from ansible-doc is considered an error.

Command "ansible-doc -l --json -t filter ovirt.ovirt" returned exit status 0.
>>> Standard Error
[WARNING]: Skipping file
b'/root/ansible_collections/ovirt/ovirt/plugins/filter/convert_to_bytes.py':
"Failed to load
b'/root/ansible_collections/ovirt/ovirt/plugins/filter/convert_to_bytes.py' for
ovirt.ovirt: invalid syntax (convert_to_bytes.py, line 4)"
[WARNING]: Skipping filter plugins in ovirt.ovirt.convert_to_bytes'; an error
occurred while loading: invalid syntax (convert_to_bytes.py, line 4)
```

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 59 errors:

``` text
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.10` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 60 errors:

``` text
plugins/filter/convert_to_bytes.py:4:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import convert_to_bytes
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.11` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 60 errors:

``` text
plugins/filter/convert_to_bytes.py:4:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import convert_to_bytes
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.12` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 60 errors:

``` text
plugins/filter/convert_to_bytes.py:4:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import convert_to_bytes
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.6` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 59 errors:

``` text
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 59 errors:

``` text
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.8` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 59 errors:

``` text
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test compile --python 3.9` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 59 errors:

``` text
plugins/module_utils/ovirt.py:31:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.cloud import CloudRetry
plugins/modules/ovirt_affinity_group.py:149:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_affinity_label_info.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_api_info.py:61:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_auth.py:220:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import check_sdk
plugins/modules/ovirt_cluster.py:385:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_cluster_info.py:83:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter.py:167:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_datacenter_info.py:67:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk.py:390:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_disk_profile.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event.py:138:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_event_info.py:108:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider.py:207:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_external_provider_info.py:103:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_group_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host.py:329:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_network.py:230:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_pm.py:130:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_host_storage_info.py:117:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_instance_type.py:287:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_job.py:120:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_mac_pool.py:98:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network.py:179:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_network_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic.py:174:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_nic_info.py:94:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission.py:160:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_permission_info.py:102:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_qos.py:242:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota.py:166:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_quota_info.py:86:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_role.py:85:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_scheduling_policy_info.py:87:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot.py:215:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_snapshot_info.py:78:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_connection.py:135:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain.py:423:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_domain_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_template_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_storage_vm_info.py:92:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_system_option_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag.py:136:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_tag_info.py:104:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template.py:595:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_template_info.py:84:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user.py:113:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_user_info.py:80:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm.py:1393:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_info.py:127:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vm_os_info.py:91:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool.py:239:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vmpool_info.py:82:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile.py:156:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
plugins/modules/ovirt_vnic_profile_info.py:81:26: SyntaxError: from ansible_collections.@NAMESPACE@.@NAME@.plugins.module_utils.ovirt import (
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 66 errors:

``` text
plugins/callback/stdout.py:0:0: invalid-documentation: DOCUMENTATION.callback: extra keys not allowed @ data['callback']. Got 'stdout'
plugins/callback/stdout.py:0:0: invalid-documentation: DOCUMENTATION.callback_type: extra keys not allowed @ data['callback_type']. Got 'aggregate'
plugins/callback/stdout.py:0:0: invalid-documentation: DOCUMENTATION.name: required key not provided @ data['name']. Got None
plugins/callback/stdout.py:0:0: invalid-documentation: DOCUMENTATION.type: required key not provided @ data['type']. Got None
plugins/callback/stdout.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/callback/stdout.py:6:0: import-before-documentation: Import found before documentation variables. All imports must appear below DOCUMENTATION/EXAMPLES/RETURN.
plugins/inventory/ovirt.py:0:0: invalid-documentation: DOCUMENTATION.plugin_type: extra keys not allowed @ data['plugin_type']. Got 'inventory'
plugins/inventory/ovirt.py:0:0: parameter-list-no-elements: DOCUMENTATION.options.ovirt_hostname_preference: Argument defines type as list but elements is not defined for dictionary value @ data['options']['ovirt_hostname_preference']. Got {'required': False, 'description': ['List of options that describe the ordering for which hostnames should be assigned.', 'See U(https://ovirt.github.io/ovirt-engine-api-model/master/#types/vm) for available attributes.'], 'default': ['fqdn', 'name'], 'type': 'list'}
plugins/modules/ovirt_affinity_group.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_affinity_label.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_affinity_label_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_api_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_auth.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_cluster.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_cluster_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_datacenter.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_datacenter_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_disk.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_disk_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_disk_profile.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_event.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_event_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_external_provider.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_external_provider_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_group.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_group_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_host.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_host_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_host_network.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_host_pm.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_host_storage_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_instance_type.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_job.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_mac_pool.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_network.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_network_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_nic.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_nic_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_permission.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_permission_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_qos.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_quota.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_quota_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_role.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_scheduling_policy_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_snapshot.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_snapshot_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_storage_connection.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_storage_domain.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_storage_domain_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_storage_template_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_storage_vm_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_system_option_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_tag.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_tag_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_template.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_template_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_user.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_user_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vm.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vm_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vm_os_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vmpool.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vmpool_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vnic_profile.py:0:0: python-syntax-error: Python SyntaxError while parsing module
plugins/modules/ovirt_vnic_profile_info.py:0:0: python-syntax-error: Python SyntaxError while parsing module
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/yamllint.html)] failed with 113 errors:

``` text
examples/filters/ovirtdiff.yml:33:7: error: syntax error: found character '@' that cannot start any token (syntax)
examples/filters/ovirtdiff.yml:33:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
examples/filters/vmips.yml:77:7: error: syntax error: found character '@' that cannot start any token (syntax)
examples/filters/vmips.yml:77:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
examples/ovirt_ansible_collections.yml:21:7: error: syntax error: found character '@' that cannot start any token (syntax)
examples/ovirt_ansible_collections.yml:21:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
plugins/filter/convert_to_bytes.py:4:26: python-syntax-error: invalid syntax (<unknown>, line 4)
plugins/inventory/ovirt.py:67:9: error: EXAMPLES: syntax error: found character '@' that cannot start any token (syntax)
plugins/inventory/ovirt.py:67:9: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
plugins/modules/ovirt_affinity_group.py:149:26: python-syntax-error: invalid syntax (<unknown>, line 149)
plugins/modules/ovirt_affinity_label.py:113:26: python-syntax-error: invalid syntax (<unknown>, line 113)
plugins/modules/ovirt_affinity_label_info.py:113:26: python-syntax-error: invalid syntax (<unknown>, line 113)
plugins/modules/ovirt_api_info.py:61:26: python-syntax-error: invalid syntax (<unknown>, line 61)
plugins/modules/ovirt_auth.py:220:26: python-syntax-error: invalid syntax (<unknown>, line 220)
plugins/modules/ovirt_cluster.py:385:26: python-syntax-error: invalid syntax (<unknown>, line 385)
plugins/modules/ovirt_cluster_info.py:83:26: python-syntax-error: invalid syntax (<unknown>, line 83)
plugins/modules/ovirt_datacenter.py:167:26: python-syntax-error: invalid syntax (<unknown>, line 167)
plugins/modules/ovirt_datacenter_info.py:67:26: python-syntax-error: invalid syntax (<unknown>, line 67)
plugins/modules/ovirt_disk.py:390:26: python-syntax-error: invalid syntax (<unknown>, line 390)
plugins/modules/ovirt_disk_info.py:81:26: python-syntax-error: invalid syntax (<unknown>, line 81)
plugins/modules/ovirt_disk_profile.py:104:26: python-syntax-error: invalid syntax (<unknown>, line 104)
plugins/modules/ovirt_event.py:138:26: python-syntax-error: invalid syntax (<unknown>, line 138)
plugins/modules/ovirt_event_info.py:108:26: python-syntax-error: invalid syntax (<unknown>, line 108)
plugins/modules/ovirt_external_provider.py:207:26: python-syntax-error: invalid syntax (<unknown>, line 207)
plugins/modules/ovirt_external_provider_info.py:103:26: python-syntax-error: invalid syntax (<unknown>, line 103)
plugins/modules/ovirt_group.py:104:26: python-syntax-error: invalid syntax (<unknown>, line 104)
plugins/modules/ovirt_group_info.py:80:26: python-syntax-error: invalid syntax (<unknown>, line 80)
plugins/modules/ovirt_host.py:329:26: python-syntax-error: invalid syntax (<unknown>, line 329)
plugins/modules/ovirt_host_info.py:86:26: python-syntax-error: invalid syntax (<unknown>, line 86)
plugins/modules/ovirt_host_network.py:230:26: python-syntax-error: invalid syntax (<unknown>, line 230)
plugins/modules/ovirt_host_pm.py:130:26: python-syntax-error: invalid syntax (<unknown>, line 130)
plugins/modules/ovirt_host_storage_info.py:117:26: python-syntax-error: invalid syntax (<unknown>, line 117)
plugins/modules/ovirt_instance_type.py:287:26: python-syntax-error: invalid syntax (<unknown>, line 287)
plugins/modules/ovirt_job.py:120:26: python-syntax-error: invalid syntax (<unknown>, line 120)
plugins/modules/ovirt_mac_pool.py:98:26: python-syntax-error: invalid syntax (<unknown>, line 98)
plugins/modules/ovirt_network.py:179:26: python-syntax-error: invalid syntax (<unknown>, line 179)
plugins/modules/ovirt_network_info.py:84:26: python-syntax-error: invalid syntax (<unknown>, line 84)
plugins/modules/ovirt_nic.py:174:26: python-syntax-error: invalid syntax (<unknown>, line 174)
plugins/modules/ovirt_nic_info.py:94:26: python-syntax-error: invalid syntax (<unknown>, line 94)
plugins/modules/ovirt_permission.py:160:26: python-syntax-error: invalid syntax (<unknown>, line 160)
plugins/modules/ovirt_permission_info.py:102:26: python-syntax-error: invalid syntax (<unknown>, line 102)
plugins/modules/ovirt_qos.py:242:26: python-syntax-error: invalid syntax (<unknown>, line 242)
plugins/modules/ovirt_quota.py:166:26: python-syntax-error: invalid syntax (<unknown>, line 166)
plugins/modules/ovirt_quota_info.py:86:26: python-syntax-error: invalid syntax (<unknown>, line 86)
plugins/modules/ovirt_role.py:85:26: python-syntax-error: invalid syntax (<unknown>, line 85)
plugins/modules/ovirt_scheduling_policy_info.py:87:26: python-syntax-error: invalid syntax (<unknown>, line 87)
plugins/modules/ovirt_snapshot.py:215:26: python-syntax-error: invalid syntax (<unknown>, line 215)
plugins/modules/ovirt_snapshot_info.py:78:26: python-syntax-error: invalid syntax (<unknown>, line 78)
plugins/modules/ovirt_storage_connection.py:135:26: python-syntax-error: invalid syntax (<unknown>, line 135)
plugins/modules/ovirt_storage_domain.py:423:26: python-syntax-error: invalid syntax (<unknown>, line 423)
plugins/modules/ovirt_storage_domain_info.py:84:26: python-syntax-error: invalid syntax (<unknown>, line 84)
plugins/modules/ovirt_storage_template_info.py:92:26: python-syntax-error: invalid syntax (<unknown>, line 92)
plugins/modules/ovirt_storage_vm_info.py:92:26: python-syntax-error: invalid syntax (<unknown>, line 92)
plugins/modules/ovirt_system_option_info.py:81:26: python-syntax-error: invalid syntax (<unknown>, line 81)
plugins/modules/ovirt_tag.py:136:26: python-syntax-error: invalid syntax (<unknown>, line 136)
plugins/modules/ovirt_tag_info.py:104:26: python-syntax-error: invalid syntax (<unknown>, line 104)
plugins/modules/ovirt_template.py:595:26: python-syntax-error: invalid syntax (<unknown>, line 595)
plugins/modules/ovirt_template_info.py:84:26: python-syntax-error: invalid syntax (<unknown>, line 84)
plugins/modules/ovirt_user.py:113:26: python-syntax-error: invalid syntax (<unknown>, line 113)
plugins/modules/ovirt_user_info.py:80:26: python-syntax-error: invalid syntax (<unknown>, line 80)
plugins/modules/ovirt_vm.py:1393:26: python-syntax-error: invalid syntax (<unknown>, line 1393)
plugins/modules/ovirt_vm_info.py:127:26: python-syntax-error: invalid syntax (<unknown>, line 127)
plugins/modules/ovirt_vm_os_info.py:91:26: python-syntax-error: invalid syntax (<unknown>, line 91)
plugins/modules/ovirt_vmpool.py:239:26: python-syntax-error: invalid syntax (<unknown>, line 239)
plugins/modules/ovirt_vmpool_info.py:82:26: python-syntax-error: invalid syntax (<unknown>, line 82)
plugins/modules/ovirt_vnic_profile.py:156:26: python-syntax-error: invalid syntax (<unknown>, line 156)
plugins/modules/ovirt_vnic_profile_info.py:81:26: python-syntax-error: invalid syntax (<unknown>, line 81)
roles/cluster_upgrade/examples/cluster_upgrade.yml:26:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/cluster_upgrade/examples/cluster_upgrade.yml:26:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/disaster_recovery/examples/dr_ovirt_setup.yml:11:8: error: syntax error: found character '@' that cannot start any token (syntax)
roles/disaster_recovery/examples/dr_ovirt_setup.yml:11:8: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/disaster_recovery/examples/dr_play.yml:8:8: error: syntax error: found character '@' that cannot start any token (syntax)
roles/disaster_recovery/examples/dr_play.yml:8:8: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/engine_setup/examples/engine-deploy.yml:18:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/engine_setup/examples/engine-deploy.yml:18:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/engine_setup/examples/engine-upgrade.yml:19:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/engine_setup/examples/engine-upgrade.yml:19:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/engine_setup/tests/engine-deploy.yml:17:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/engine_setup/tests/engine-deploy.yml:17:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/engine_setup/tests/engine-upgrade.yml:17:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/engine_setup/tests/engine-upgrade.yml:17:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/hosted_engine_setup/examples/hosted_engine_deploy_localhost.yml:8:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/hosted_engine_setup/examples/hosted_engine_deploy_localhost.yml:8:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/hosted_engine_setup/examples/hosted_engine_deploy_remotehost.yml:7:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/hosted_engine_setup/examples/hosted_engine_deploy_remotehost.yml:7:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/hosted_engine_setup/tasks/full_execution.yml:45:15: error: syntax error: found character '@' that cannot start any token (syntax)
roles/hosted_engine_setup/tasks/full_execution.yml:45:15: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/hosted_engine_setup/tasks/partial_execution.yml:65:19: error: syntax error: found character '@' that cannot start any token (syntax)
roles/hosted_engine_setup/tasks/partial_execution.yml:65:19: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/image_template/examples/ovirt_image_template.yml:27:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/image_template/examples/ovirt_image_template.yml:27:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/infra/examples/ovirt_infra.yml:15:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/infra/examples/ovirt_infra.yml:15:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/infra/examples/ovirt_infra_destroy.yml:43:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/infra/examples/ovirt_infra_destroy.yml:43:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/infra/roles/datacenters/tasks/main.yml:25:11: error: syntax error: found character '@' that cannot start any token (syntax)
roles/infra/roles/datacenters/tasks/main.yml:25:11: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/infra/tasks/create_infra.yml:4:11: error: syntax error: found character '@' that cannot start any token (syntax)
roles/infra/tasks/create_infra.yml:4:11: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/infra/tasks/remove_infra.yml:4:11: error: syntax error: found character '@' that cannot start any token (syntax)
roles/infra/tasks/remove_infra.yml:4:11: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/remove_stale_lun/examples/remove_stale_lun.yml:19:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/remove_stale_lun/examples/remove_stale_lun.yml:19:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/repositories/examples/ovirt_repositories_release_rpm.yml:11:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/repositories/examples/ovirt_repositories_release_rpm.yml:11:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/repositories/examples/ovirt_repositories_subscription_manager.yml:22:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/repositories/examples/ovirt_repositories_subscription_manager.yml:22:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/shutdown_env/examples/shutdown_env.yml:18:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/shutdown_env/examples/shutdown_env.yml:18:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/vm_infra/examples/ovirt_vm_infra.yml:48:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/vm_infra/examples/ovirt_vm_infra.yml:48:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
roles/vm_infra/examples/ovirt_vm_infra_inv.yml:51:7: error: syntax error: found character '@' that cannot start any token (syntax)
roles/vm_infra/examples/ovirt_vm_infra_inv.yml:51:7: unparsable-with-libyaml: while scanning for the next token - found character that cannot start any token
```



## File divergences

The following files differ between the `3.2.0-1` git tag and `ovirt-ovirt-3.2.0.tar.gz` on Ansible Galaxy:

- `galaxy.yml` (`WRONG_GALAXY_YML_NAME` : `@NAMESPACE@.@NAME@` != `ovirt.ovirt`)
- `build.sh` (`WRONG_HASH`)
- `CHANGELOG.rst` (`WRONG_HASH`)
- `examples/filters/ovirtdiff.yml` (`WRONG_HASH`)
- `examples/filters/vmips.yml` (`WRONG_HASH`)
- `examples/ovirt_ansible_collections.yml` (`WRONG_HASH`)
- `README.md` (`WRONG_HASH`)
- `roles/repositories/examples/ovirt_repositories_release_rpm.yml` (`WRONG_HASH`)
- `roles/repositories/examples/ovirt_repositories_subscription_manager.yml` (`WRONG_HASH`)
- `roles/repositories/README.md` (`WRONG_HASH`)
- `roles/cluster_upgrade/examples/cluster_upgrade.yml` (`WRONG_HASH`)
- `roles/cluster_upgrade/README.md` (`WRONG_HASH`)
- `roles/shutdown_env/examples/shutdown_env.yml` (`WRONG_HASH`)
- `roles/shutdown_env/README.md` (`WRONG_HASH`)
- `roles/disaster_recovery/examples/dr_ovirt_setup.yml` (`WRONG_HASH`)
- `roles/disaster_recovery/examples/dr_play.yml` (`WRONG_HASH`)
- `roles/disaster_recovery/README.md` (`WRONG_HASH`)
- `roles/vm_infra/tasks/create_inventory.yml` (`WRONG_HASH`)
- `roles/vm_infra/tasks/main.yml` (`WRONG_HASH`)
- `roles/vm_infra/tasks/vm_state_present.yml` (`WRONG_HASH`)
- `roles/vm_infra/examples/ovirt_vm_infra_inv.yml` (`WRONG_HASH`)
- `roles/vm_infra/examples/ovirt_vm_infra.yml` (`WRONG_HASH`)
- `roles/vm_infra/README.md` (`WRONG_HASH`)
- `roles/image_template/tasks/qcow2_image.yml` (`WRONG_HASH`)
- `roles/image_template/tasks/glance_image.yml` (`WRONG_HASH`)
- `roles/image_template/examples/ovirt_image_template.yml` (`WRONG_HASH`)
- `roles/image_template/README.md` (`WRONG_HASH`)
- `roles/engine_setup/tests/engine-deploy.yml` (`WRONG_HASH`)
- `roles/engine_setup/tests/engine-upgrade.yml` (`WRONG_HASH`)
- `roles/engine_setup/examples/engine-deploy.yml` (`WRONG_HASH`)
- `roles/engine_setup/examples/engine-upgrade.yml` (`WRONG_HASH`)
- `roles/engine_setup/README.md` (`WRONG_HASH`)
- `roles/remove_stale_lun/examples/remove_stale_lun.yml` (`WRONG_HASH`)
- `roles/remove_stale_lun/README.md` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/create_storage_domain.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/alter_libvirt_default_net_configuration.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/bootstrap_local_vm/02_create_local_vm.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/pre_checks/002_validate_hostname_tasks.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/partial_execution.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/full_execution.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/create_target_vm/03_hosted_engine_final_tasks.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/tasks/create_target_vm/01_create_target_hosted_engine_vm.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/examples/hosted_engine_deploy_remotehost.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/examples/hosted_engine_deploy_localhost.yml` (`WRONG_HASH`)
- `roles/hosted_engine_setup/README.md` (`WRONG_HASH`)
- `roles/infra/tasks/create_infra.yml` (`WRONG_HASH`)
- `roles/infra/tasks/remove_infra.yml` (`WRONG_HASH`)
- `roles/infra/examples/ovirt_infra.yml` (`WRONG_HASH`)
- `roles/infra/examples/ovirt_infra_destroy.yml` (`WRONG_HASH`)
- `roles/infra/README.md` (`WRONG_HASH`)
- `roles/infra/roles/datacenter_cleanup/README.md` (`WRONG_HASH`)
- `roles/infra/roles/permissions/README.md` (`WRONG_HASH`)
- `roles/infra/roles/clusters/README.md` (`WRONG_HASH`)
- `roles/infra/roles/mac_pools/README.md` (`WRONG_HASH`)
- `roles/infra/roles/hosts/tasks/main.yml` (`WRONG_HASH`)
- `roles/infra/roles/hosts/README.md` (`WRONG_HASH`)
- `roles/infra/roles/networks/README.md` (`WRONG_HASH`)
- `roles/infra/roles/datacenters/tasks/main.yml` (`WRONG_HASH`)
- `roles/infra/roles/datacenters/README.md` (`WRONG_HASH`)
- `roles/infra/roles/aaa_jdbc/README.md` (`WRONG_HASH`)
- `roles/infra/roles/external_providers/README.md` (`WRONG_HASH`)
- `roles/infra/roles/storages/README.md` (`WRONG_HASH`)
- `changelogs/changelog.yaml` (`WRONG_HASH`)
- `ovirt-ansible-collection.spec.in` (`WRONG_HASH`)
- `plugins/inventory/ovirt.py` (`WRONG_HASH`)
- `plugins/filter/convert_to_bytes.py` (`WRONG_HASH`)
- `plugins/filter/ovirtvmipv6.yml` (`WRONG_HASH`)
- `plugins/filter/convert_to_bytes.yml` (`WRONG_HASH`)
- `plugins/filter/removesensitivevmdata.yml` (`WRONG_HASH`)
- `plugins/filter/get_ovf_disk_size.yml` (`WRONG_HASH`)
- `plugins/filter/ovirtvmipsv4.yml` (`WRONG_HASH`)
- `plugins/filter/filtervalue.yml` (`WRONG_HASH`)
- `plugins/filter/ovirtdiff.yml` (`WRONG_HASH`)
- `plugins/filter/ovirtvmips.yml` (`WRONG_HASH`)
- `plugins/filter/get_network_xml_to_dict.yml` (`WRONG_HASH`)
- `plugins/filter/ovirtvmip.yml` (`WRONG_HASH`)
- `plugins/filter/ovirtvmipsv6.yml` (`WRONG_HASH`)
- `plugins/filter/ovirtvmipv4.yml` (`WRONG_HASH`)
- `plugins/module_utils/ovirt.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_user_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vm_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_disk.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_template_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_api_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_nic.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_snapshot.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_storage_vm_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_network_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_nic_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_mac_pool.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_instance_type.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_job.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_host_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_template.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vnic_profile_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_storage_connection.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vmpool_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_quota_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vm.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_cluster_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_tag_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_permission.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_host_network.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_external_provider_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_event_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_disk_profile.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_storage_domain_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_tag.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vm_os_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_quota.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_affinity_label.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_role.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_group_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_host_pm.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_external_provider.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_host_storage_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_snapshot_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_qos.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_datacenter.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_affinity_group.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vnic_profile.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_permission_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_host.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_disk_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_cluster.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_datacenter_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_user.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_system_option_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_vmpool.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_network.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_affinity_label_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_storage_template_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_storage_domain.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_event.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_auth.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_scheduling_policy_info.py` (`WRONG_HASH`)
- `plugins/modules/ovirt_group.py` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
