# Community package requirements: repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)


The contents in the `v1.0.0` git tag do not match `hitachivantara-vspone_object-1.0.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---


## File divergences

The following files differ between the `v1.0.0` git tag and `hitachivantara-vspone_object-1.0.0.tar.gz` on Ansible Galaxy:

- `README.md` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_s3_encryption_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_licenses_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_user_buckets_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_class_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_class.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_events_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_galaxy_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_s3_user_credentials.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_troubleshooting_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_serial_number.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_jobs_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_kmip.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_component.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_certificates.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_users_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_region_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_certificates_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_license.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_s3_encryption.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_fault_domain.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_fault_domain_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_user_id_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_components_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_kmip_server_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_storage_component_state_update.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_job.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_serial_number_facts.py` (`WRONG_HASH`)
- `plugins/modules/oneobject_node/hv_csrf.py` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
