# Community package requirements: sanity tests and repository management

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `2.1.0` of `kubevirt.core`, corresponding to the `2.1.0` tag in this repo, fails one or more of the required sanity tests.

The contents in the `2.1.0` git tag do not match `kubevirt-core-2.1.0.tar.gz` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.19.0b1`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/devel/dev_guide/testing/sanity/validate-modules.html)] failed with 4 errors:

``` text
plugins/inventory/kubevirt.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/kubevirt_vm.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/kubevirt_vm_info.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/kubevirt_vmi_info.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
```



## File divergences

The following files differ between the `2.1.0` git tag and `kubevirt-core-2.1.0.tar.gz` on Ansible Galaxy:

- `docs/CHANGELOG.rst` (`WRONG_HASH`)
- `CHANGELOG.rst` (`WRONG_HASH`)


[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
