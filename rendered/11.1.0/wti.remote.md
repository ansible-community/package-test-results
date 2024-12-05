# Community package requirements: repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)


The contents in the `v1.0.10` git tag do not match `wti-remote-1.0.10.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---


## File divergences

The following files differ between the `v1.0.10` git tag and `wti-remote-1.0.10.tar.gz` on Ansible Galaxy:

- `meta/runtime.yml` (`WRONG_HASH`)
- `plugins/modules/cpm_web_config.py` (`WRONG_HASH`)
- `plugins/modules/cpm_syslog_client_config.py` (`WRONG_HASH`)
- `plugins/modules/cpm_hostname_config.py` (`WRONG_HASH`)
- `plugins/modules/cpm_config_backup.py` (`WRONG_HASH`)
- `plugins/modules/cpm_config_restore.py` (`WRONG_HASH`)
- `README.md` (`WRONG_HASH`)
- `playbooks/cpm_config/cpm_config_backup.yml` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
