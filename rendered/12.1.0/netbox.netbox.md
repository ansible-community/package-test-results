# Community package requirements: repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)


The contents in the `v3.21.0` git tag do not match `netbox-netbox-3.21.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---


## File divergences

The following files differ between the `v3.21.0` git tag and `netbox-netbox-3.21.0.tar.gz` on Ansible Galaxy:

- `docs/getting_started/contributing/modules/architecture.rst` (`WRONG_HASH`)
- `docs/plugins/nb_lookup_lookup.rst` (`WRONG_HASH`)
- `docs/plugins/netbox_platform_module.rst` (`WRONG_HASH`)
- `docs/plugins/netbox_prefix_module.rst` (`WRONG_HASH`)
- `docs/plugins/netbox_device_type_module.rst` (`WRONG_HASH`)
- `poetry.lock` (`WRONG_HASH`)
- `.github/workflows/main.yml` (`WRONG_HASH`)
- `tests/integration/targets/v4.2/tasks/netbox_circuit_termination.yml` (`WRONG_HASH`)
- `tests/integration/targets/v4.2/tasks/netbox_service.yml` (`WRONG_HASH`)
- `tests/integration/targets/v4.2/tasks/netbox_tag.yml` (`WRONG_HASH`)
- `tests/integration/targets/inventory-v4.2/compare_inventory_json.py` (`WRONG_HASH`)
- `tests/integration/targets/inventory-v4.1/compare_inventory_json.py` (`WRONG_HASH`)
- `tests/unit/module_utils/test_netbox_base_class.py` (`WRONG_HASH`)
- `plugins/modules/netbox_circuit_termination.py` (`WRONG_HASH`)
- `plugins/modules/netbox_platform.py` (`WRONG_HASH`)
- `plugins/modules/netbox_device_type.py` (`WRONG_HASH`)
- `plugins/modules/netbox_prefix.py` (`WRONG_HASH`)
- `plugins/modules/netbox_custom_field.py` (`WRONG_HASH`)
- `plugins/modules/netbox_tag.py` (`WRONG_HASH`)
- `plugins/lookup/nb_lookup.py` (`WRONG_HASH`)
- `plugins/inventory/nb_inventory.py` (`WRONG_HASH`)
- `plugins/module_utils/netbox_dcim.py` (`WRONG_HASH`)
- `plugins/module_utils/netbox_ipam.py` (`WRONG_HASH`)
- `plugins/module_utils/netbox_utils.py` (`WRONG_HASH`)
- `plugins/doc_fragments/common.py` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
