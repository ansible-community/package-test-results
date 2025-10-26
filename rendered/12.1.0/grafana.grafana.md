# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `6.0.4` of `grafana.grafana`, corresponding to the `6.0.4` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/validate-modules.html)] failed with 8 errors:

``` text
plugins/modules/cloud_stack.py:0:0: doc-default-does-not-match-spec: Argument 'delete_protection' in argument_spec defines default as (None) but documentation defines default as (True)
plugins/modules/cloud_stack.py:0:0: doc-type-does-not-match-spec: Argument 'delete_protection' in argument_spec defines type as <class 'bool'> but documentation defines type as 'bool'
plugins/modules/user.py:0:0: doc-choices-do-not-match-spec: Argument 'state' in argument_spec defines choices as (['present', 'absent', 'update_password']) but documentation defines choices as (['present', 'absent'])
plugins/modules/user.py:0:0: invalid-documentation: DOCUMENTATION.author: Invalid author for dictionary value @ data['author']. Got ['Mathieu Valois, téïcée']
plugins/modules/user.py:0:0: parameter-type-not-in-doc: Argument 'orgid' in argument_spec defines type as 'int' but documentation doesn't define type
plugins/modules/user.py:0:0: undocumented-parameter: Argument 'orgid' is listed in the argument_spec, but not documented in the module documentation
plugins/modules/user.py:8:0: import-before-documentation: Import found before documentation variables. All imports must appear below DOCUMENTATION/EXAMPLES/RETURN.
plugins/modules/user.py:73:12: invalid-examples: EXAMPLES is not valid YAML
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/yamllint.html)] failed with 4 errors:

``` text
plugins/modules/user.py:73:12: error: EXAMPLES: syntax error: expected <block end>, but found '<scalar>' (syntax)
plugins/modules/user.py:73:12: unparsable-with-libyaml: EXAMPLES: while parsing a block mapping did not find expected key
roles/grafana/tasks/install.yml:31:26: colons: too many spaces before colon
roles/mimir/defaults/main.yml:25:1: empty-lines: too many blank lines (1 > 0)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
