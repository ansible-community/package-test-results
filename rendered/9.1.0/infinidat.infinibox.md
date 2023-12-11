# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.3.12` of `infinidat.infinibox`, corresponding to the `v1.3.12` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 1 error:

``` text
plugins/modules/infini_vol.py:524:155: SyntaxError: msg = f"An error has occurred handling volume_type '{module.params['volume_type']}' or write_protected '{module.params['write_protected']}' values"
```

The test `ansible-test sanity --test compile --python 3.10` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 3 errors:

``` text
bin/check_collection_files.sh:3:8: SyntaxError: set -o nounset
bin/install_modules_for_hacking.sh:11:8: SyntaxError: set -o nounset
bin/test_summarize.sh:3:8: SyntaxError: set -o nounset
```

The test `ansible-test sanity --test compile --python 3.11` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 3 errors:

``` text
bin/check_collection_files.sh:3:8: SyntaxError: set -o nounset
bin/install_modules_for_hacking.sh:11:8: SyntaxError: set -o nounset
bin/test_summarize.sh:3:8: SyntaxError: set -o nounset
```

The test `ansible-test sanity --test compile --python 3.12` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 3 errors:

``` text
bin/check_collection_files.sh:3:8: SyntaxError: set -o nounset
bin/install_modules_for_hacking.sh:11:8: SyntaxError: set -o nounset
bin/test_summarize.sh:3:8: SyntaxError: set -o nounset
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/validate-modules.html)] failed with 24 errors:

``` text
plugins/modules/infini_fs.py:0:0: doc-type-does-not-match-spec: Argument 'thin_provision' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_host.py:0:0: import-error: Exception attempting to import module for argument_spec introspection, 'No module named 'infi''
plugins/modules/infini_map.py:0:0: doc-default-does-not-match-spec: Argument 'cluster' in argument_spec defines default as ('') but documentation defines default as (None)
plugins/modules/infini_map.py:0:0: doc-default-does-not-match-spec: Argument 'host' in argument_spec defines default as ('') but documentation defines default as (None)
plugins/modules/infini_map.py:0:0: doc-missing-type: Argument 'cluster' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_map.py:0:0: doc-missing-type: Argument 'host' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_map.py:0:0: doc-missing-type: Argument 'volume' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_map.py:0:0: parameter-type-not-in-doc: Argument 'lun' in argument_spec defines type as <class 'int'> but documentation doesn't define type
plugins/modules/infini_network_space.py:0:0: doc-choices-do-not-match-spec: Argument 'service' in argument_spec defines choices as (['replication', 'NAS_SERVICE', 'ISCSI_SERVICE']) but documentation defines choices as (['replication', 'NAS', 'iSCSI'])
plugins/modules/infini_network_space.py:0:0: doc-default-does-not-match-spec: Argument 'interfaces' in argument_spec defines default as ([]) but documentation defines default as (None)
plugins/modules/infini_network_space.py:0:0: doc-default-does-not-match-spec: Argument 'network_config' in argument_spec defines default as ({}) but documentation defines default as (None)
plugins/modules/infini_network_space.py:0:0: doc-elements-mismatch: Argument 'interfaces' in argument_spec specifies elements as int,but elements is documented as being str
plugins/modules/infini_network_space.py:0:0: doc-missing-type: Argument 'default_gateway' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_network_space.py:0:0: doc-missing-type: Argument 'name' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_network_space.py:0:0: doc-missing-type: Argument 'service' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_network_space.py:0:0: doc-missing-type: Argument 'state' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_network_space.py:0:0: doc-type-does-not-match-spec: Argument 'mtu' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_network_space.py:0:0: doc-type-does-not-match-spec: Argument 'netmask' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_network_space.py:0:0: doc-type-does-not-match-spec: Argument 'rate_limit' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_network_space.py:0:0: parameter-type-not-in-doc: Argument 'network_config' in argument_spec defines type as <class 'dict'> but documentation doesn't define type
plugins/modules/infini_network_space.py:0:0: undocumented-parameter: Argument 'default_gateway' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/infini_network_space.py:0:0: undocumented-parameter: Argument 'network_config' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/infini_port.py:0:0: parameter-type-not-in-doc: Argument 'host' in argument_spec defines type as <class 'str'> but documentation doesn't define type
plugins/modules/infini_vol.py:0:0: import-error: Exception attempting to import module for argument_spec introspection, 'cannot import name 'ObjectNotFound' from 'ansible_collections.infinidat.infinibox.plugins.module_utils.infinibox' (/root/ansible_collections/infinidat/infinibox/plugins/module_utils/infinibox.py)'
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
