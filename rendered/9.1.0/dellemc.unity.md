# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.7.1` of `dellemc.unity`, corresponding to the `1.7.1` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 3 errors:

``` text
plugins/modules/filesystem.py:1419:60: SyntaxError: errormsg = f"Invalid rpo value - {rpo} for " \
plugins/modules/nfs.py:1074:54: SyntaxError: msg = f'Host : {host} does not exists'
plugins/modules/replication_session.py:331:94: SyntaxError: errormsg = f"Retrieving details of replication session {id_or_name} failed with error"
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 18 errors:

``` text
plugins/modules/cifsserver.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/consistencygroup.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/filesystem.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/filesystem_snapshot.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/host.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/info.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/interface.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/nasserver.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/nfs.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/nfsserver.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/replication_session.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/smbshare.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/snapshot.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/snapshotschedule.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/storagepool.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/tree_quota.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/user_quota.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
plugins/modules/volume.py:0:0: missing-gplv3-license: GPLv3 license header not found in the first 20 lines of the module
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
