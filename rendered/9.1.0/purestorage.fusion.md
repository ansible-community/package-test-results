# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.6.0` of `purestorage.fusion`, corresponding to the `1.6.0` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 6 errors:

``` text
plugins/module_utils/fusion.py:71:84: SyntaxError: f"{old_env} env variable is ignored because {new_env} is specified."
plugins/modules/fusion_info.py:104:86: SyntaxError: module.warn(f"Cannot get [{name} dict], reason: Permission denied")
plugins/modules/fusion_nig.py:180:86: SyntaxError: module.warn(f"group_type={module.params['group_type']} is not implemented")
plugins/modules/fusion_sc.py:157:51: SyntaxError: if iops_limit < 100 or iops_limit > 100_000_000:
plugins/modules/fusion_se.py:444:96: SyntaxError: f"'{param_name}' parameter is deprecated and will be removed in the version 2.0"
plugins/modules/fusion_volume.py:425:81: SyntaxError: return f"/tenants/{tenant}/tenant-spaces/{tenant_space}/volumes/{volume}"
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
