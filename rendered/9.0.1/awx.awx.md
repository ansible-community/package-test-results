# Community package requirements: repository management

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)


The contents in the `23.3.1` git tag do not match `awx-awx-23.3.1.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---


## File divergences

The following files differ between the `23.3.1` git tag and `awx-awx-23.3.1.tar.gz` on Ansible Galaxy:

- `README.md` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
