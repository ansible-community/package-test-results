# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.1.4` of `hpe.nimble`, corresponding to the `v1.1.4` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 23 errors:

``` text
plugins/module_utils/hpe_nimble.py:171:66: SyntaxError: raise Exception(f"Invalid value for volume {vol_name}")
plugins/modules/hpe_nimble_access_control_record.py:125:97: SyntaxError: return (False, False, f"Initiator Group '{initiator_group}' is not present on array.", {})
plugins/modules/hpe_nimble_array.py:199:81: SyntaxError: return (True, True, f"Created array '{array_name}' successfully.", {}, array_resp.attrs)
plugins/modules/hpe_nimble_chap_user.py:123:80: SyntaxError: return (True, True, f"Chap user '{user_name}' created successfully.", {}, user_resp.attrs)
plugins/modules/hpe_nimble_disk.py:116:115: SyntaxError: return (True, True, f"Successfully updated disk to slot '{slot}' at shelf location '{shelf_location}'.", changed_attrs_dict, disk_resp)
plugins/modules/hpe_nimble_encryption.py:150:82: SyntaxError: return (True, True, f"Master key '{master_key}' created successfully.", {}, master_key_resp.attrs)
plugins/modules/hpe_nimble_fc.py:146:100: SyntaxError: return (False, False, f"No fibre channel is present for array '{array_name_or_serial}'.", {}, {})
plugins/modules/hpe_nimble_group.py:547:97: SyntaxError: return (False, False, f"Group '{group_name}' cannot be updated as it is not present.", {}, {})
plugins/modules/hpe_nimble_info.py:626:84: SyntaxError: msg = f"Subset name '{key}' is not valid. Please provide a correct subset name."
plugins/modules/hpe_nimble_initiator_group.py:159:97: SyntaxError: return (True, True, f"Created initiator Group '{initiator_group_name}' successfully.", {}, ig_resp.attrs)
plugins/modules/hpe_nimble_network.py:193:80: SyntaxError: return (True, True, f"Network config '{name}' created successfully.", {}, network_resp.attrs)
plugins/modules/hpe_nimble_partner.py:210:100: SyntaxError: return (True, True, f"Replication partner '{downstream_hostname}' created successfully.", {}, upstream_repl_resp.attrs)
plugins/modules/hpe_nimble_performance_policy.py:159:100: SyntaxError: return (True, True, f"Created performance policy '{perf_policy_name}' successfully.", {}, perf_policy_resp.attrs)
plugins/modules/hpe_nimble_pool.py:141:79: SyntaxError: return (True, True, f"Created pool '{pool_name}' successfully.", {}, pool_resp.attrs)
plugins/modules/hpe_nimble_protection_schedule.py:234:99: SyntaxError: return (True, True, f"Created protection schedule '{prot_schedule_name}' successfully.", {}, prot_schedule_resp.attrs)
plugins/modules/hpe_nimble_protection_template.py:176:99: SyntaxError: return (True, True, f"Protection template '{prot_template_name}' created successfully.", {}, prot_template_resp.attrs)
plugins/modules/hpe_nimble_shelf.py:114:91: SyntaxError: return (False, False, f"Shelf serial '{shelf_serial}' is not present on array.", {})
plugins/modules/hpe_nimble_snapshot.py:155:98: SyntaxError: return (False, False, f"Volume '{vol_name}' not present on array for taking snapshot.", {}, {})
plugins/modules/hpe_nimble_snapshot_collection.py:182:133: SyntaxError: return (True, True, f"Created snapshot collection '{snapcoll_name}' for volume collection '{volcoll_name}' successfully.", {}, snapcoll_resp.attrs)
plugins/modules/hpe_nimble_user.py:163:75: SyntaxError: return (True, True, f"User '{user_name}' created successfully.", {}, user_resp.attrs)
plugins/modules/hpe_nimble_user_policy.py:124:117: SyntaxError: return (True, True, f"Updated user policy successfully with following attributes '{changed_attrs_dict}'.", changed_attrs_dict, user_resp.attrs)
plugins/modules/hpe_nimble_volume.py:345:77: SyntaxError: return (False, False, f"Volume '{vol_name}' not present to move.", {}, {})
plugins/modules/hpe_nimble_volume_collection.py:305:91: SyntaxError: return (True, True, f"Created volume collection '{volcoll_name}' successfully.", {}, volcoll_resp.attrs)
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 25 errors:

``` text
plugins/modules/hpe_nimble_access_control_record.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_array.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_chap_user.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_disk.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_encryption.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_fc.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_group.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_info.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_initiator_group.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_network.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_partner.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_performance_policy.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_pool.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_protection_schedule.py:0:0: doc-default-does-not-match-spec: Argument 'at_time' in argument_spec defines default as (None) but documentation defines default as (0)
plugins/modules/hpe_nimble_protection_schedule.py:0:0: doc-default-does-not-match-spec: Argument 'num_retain_replica' in argument_spec defines default as (None) but documentation defines default as (0)
plugins/modules/hpe_nimble_protection_schedule.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_protection_template.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_shelf.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_snapshot.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_snapshot_collection.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_user.py:0:0: doc-default-does-not-match-spec: Argument 'inactivity_timeout' in argument_spec defines default as (None) but documentation defines default as (0)
plugins/modules/hpe_nimble_user.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_user_policy.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_volume.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/hpe_nimble_volume_collection.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
