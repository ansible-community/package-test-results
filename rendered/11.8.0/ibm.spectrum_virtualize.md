# Community package requirements: repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)


The contents in the `2.0.0` git tag do not match `ibm-spectrum_virtualize-2.0.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---


## File divergences

The following files differ between the `2.0.0` git tag and `ibm-spectrum_virtualize-2.0.0.tar.gz` on Ansible Galaxy:

- `playbooks/volume_migration_on_svc_iscsi/vol_migration_vars.txt` (`WRONG_HASH`)
- `playbooks/multi_volume_create_host_mapping_zone_multipath/multiple_vol_creation_zone_map_vars.txt` (`WRONG_HASH`)
- `README.md` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
