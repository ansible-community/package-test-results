# Community package requirements: repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)


The contents in the `21.15.0` git tag do not match `netapp-storagegrid-21.15.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---


## File divergences

The following files differ between the `21.15.0` git tag and `netapp-storagegrid-21.15.0.tar.gz` on Ansible Galaxy:

- `plugins/doc_fragments/netapp.py` (`WRONG_HASH`)
- `plugins/module_utils/netapp.py` (`WRONG_HASH`)
- `plugins/modules/na_sg_org_identity_federation.py` (`WRONG_HASH`)
- `plugins/modules/na_sg_grid_account.py` (`WRONG_HASH`)
- `plugins/modules/na_sg_grid_identity_federation.py` (`WRONG_HASH`)
- `tests/unit/plugins/modules/test_na_sg_grid_identity_federation.py` (`WRONG_HASH`)
- `tests/unit/plugins/modules/test_na_sg_grid_account.py` (`WRONG_HASH`)
- `tests/unit/plugins/modules/test_na_sg_org_identity_federation.py` (`WRONG_HASH`)
- `changelogs/changelog.yaml` (`WRONG_HASH`)
- `README.md` (`WRONG_HASH`)
- `CHANGELOG.rst` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
