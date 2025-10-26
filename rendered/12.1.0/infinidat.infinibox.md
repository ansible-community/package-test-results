# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.6.3` of `infinidat.infinibox`, corresponding to the `v1.6.3` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.19.3`:

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

The test `ansible-test sanity --test ansible-doc` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/ansible-doc.html)] failed with the error:

``` text
Command "ansible-doc -t module infinidat.infinibox.infini_certificate infinidat.infinibox.infini_cluster infinidat.infinibox.infini_config infinidat.infinibox.infini_event infinidat.infinibox.infini_export infinidat.infinibox.infini_export_client infinidat.infinibox.infini_fibre_channel_switch infinidat.infinibox.infini_fs infinidat.infinibox.infini_host infinidat.infinibox.infini_infinimetrics infinidat.infinibox.infini_map infinidat.infinibox.infini_metadata infinidat.infinibox.infini_network_space infinidat.infinibox.infini_notification_rule infinidat.infinibox.infini_notification_target infinidat.infinibox.infini_pool infinidat.infinibox.infini_port infinidat.infinibox.infini_sso infinidat.infinibox.infini_user infinidat.infinibox.infini_users_repository infinidat.infinibox.infini_vol" returned exit status 1.
>>> Standard Error
[ERROR]: module infinidat.infinibox.infini_metadata Missing documentation (or could not parse documentation): module plugin 'infinidat.infinibox.infini_metadata' did not contain a DOCUMENTATION attribute in '/root/ansible_collections/infinidat/infinibox/plugins/modules/infini_metadata.py': Unable to parse documentation in python file '/root/ansible_collections/infinidat/infinibox/plugins/modules/infini_metadata.py': while scanning a simple key
  in "<unicode string>", line 8, column 5
could not find expected ':'
  in "<unicode string>", line 9, column 5
```

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/validate-modules.html)] failed with 102 errors:

``` text
plugins/modules/infini_certificate.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_certificate.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_certificate.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_certificate.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_cluster.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_cluster.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_cluster.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_cluster.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_config.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_config.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_config.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_config.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_event.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_event.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_event.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_event.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_export.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_export.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_export.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_export.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_export_client.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_export_client.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_export_client.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_export_client.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_fibre_channel_switch.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_fibre_channel_switch.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_fibre_channel_switch.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_fibre_channel_switch.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_fs.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_fs.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_fs.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_fs.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_host.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_host.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_host.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_host.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_infinimetrics.py:0:0: doc-required-mismatch: Argument 'ibox_serial' in argument_spec is not required, but is documented as being required
plugins/modules/infini_infinimetrics.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_infinimetrics.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_infinimetrics.py:0:0: nonexistent-parameter-documented: Argument 'password' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/infini_infinimetrics.py:0:0: nonexistent-parameter-documented: Argument 'system' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/infini_infinimetrics.py:0:0: nonexistent-parameter-documented: Argument 'user' is listed in DOCUMENTATION.options, but not accepted by the module argument_spec
plugins/modules/infini_map.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_map.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_map.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_map.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_metadata.py:0:0: deprecation-mismatch: "meta/runtime.yml" and DOCUMENTATION.deprecation do not agree.
plugins/modules/infini_metadata.py:0:0: doc-choices-do-not-match-spec: Argument 'object_type' in argument_spec defines choices as (['cluster', 'fs', 'fs-snap', 'host', 'pool', 'system', 'vol', 'vol-snap', '']) but documentation defines choices as ([])
plugins/modules/infini_metadata.py:0:0: doc-choices-do-not-match-spec: Argument 'state' in argument_spec defines choices as (['stat', 'present', 'absent', 'search']) but documentation defines choices as ([])
plugins/modules/infini_metadata.py:0:0: doc-default-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines default as (False) but documentation defines default as (None)
plugins/modules/infini_metadata.py:0:0: doc-default-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines default as (5) but documentation defines default as (None)
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'key' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'object_name' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'object_type' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'password' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'state' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'system' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'user' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-missing-type: Argument 'value' in argument_spec uses default type ('str') but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: doc-required-mismatch: Argument 'state' in argument_spec is required, but is not documented as being required
plugins/modules/infini_metadata.py:0:0: doc-required-mismatch: Argument 'system' in argument_spec is required, but is not documented as being required
plugins/modules/infini_metadata.py:0:0: missing-documentation: No DOCUMENTATION provided
plugins/modules/infini_metadata.py:0:0: no-log-needed: Argument 'key' in argument_spec could be a secret, though doesn't have `no_log` set
plugins/modules/infini_metadata.py:0:0: parameter-type-not-in-doc: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation doesn't define type
plugins/modules/infini_metadata.py:0:0: parameter-type-not-in-doc: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation doesn't define type
plugins/modules/infini_metadata.py:23:5: documentation-syntax-error: DOCUMENTATION is not valid YAML
plugins/modules/infini_network_space.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_network_space.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_network_space.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_network_space.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_notification_rule.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_notification_rule.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_notification_rule.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_notification_rule.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_notification_target.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_notification_target.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_notification_target.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_notification_target.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_pool.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_pool.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_pool.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_pool.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_port.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_port.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_port.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_port.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_sso.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_sso.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_sso.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_sso.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_user.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_user.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_user.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_user.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_users_repository.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_users_repository.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_users_repository.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_users_repository.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
plugins/modules/infini_vol.py:0:0: doc-required-mismatch: Argument 'password' in argument_spec is not required, but is documented as being required
plugins/modules/infini_vol.py:0:0: doc-required-mismatch: Argument 'user' in argument_spec is not required, but is documented as being required
plugins/modules/infini_vol.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/infini_vol.py:0:0: doc-type-does-not-match-spec: Argument 'stay_logged_in_minutes' in argument_spec defines type as <class 'int'> but documentation defines type as 'int'
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/yamllint.html)] failed with 2 errors:

``` text
plugins/modules/infini_metadata.py:23:5: error: DOCUMENTATION: syntax error: could not find expected ':' (syntax)
plugins/modules/infini_metadata.py:23:5: unparsable-with-libyaml: DOCUMENTATION: while scanning a simple key could not find expected ':'
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
