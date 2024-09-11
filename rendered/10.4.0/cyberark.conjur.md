# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.3.0` of `cyberark.conjur`, corresponding to the `v1.3.0` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.17.4`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.17/dev_guide/testing/sanity/validate-modules.html)] failed with 1 error:

``` text
plugins/lookup/conjur_variable.py:0:0: version-added-must-be-major-or-minor: DOCUMENTATION: version_added ('1.0.2') must be a major or minor release, not a patch release (see specification at https://semver.org/). Got {'name': 'conjur_variable', 'version_added': '1.0.2', 'short_description': 'Fetch credentials from CyberArk Conjur.', 'author': ['CyberArk BizDev (@cyberark-bizdev)'], 'description': "Retrieves credentials from Conjur using the controlling host's Conjur identity, environment variables, or extra-vars. Environment variables could be CONJUR_ACCOUNT, CONJUR_APPLIANCE_URL, CONJUR_CERT_FILE, CONJUR_AUTHN_LOGIN, CONJUR_AUTHN_API_KEY, CONJUR_AUTHN_TOKEN_FILE Extra-vars could be conjur_account, conjur...
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.17/dev_guide/testing/sanity/yamllint.html)] failed with 2 errors:

``` text
dev/policy/root.yml:2:3: unparsable-with-libyaml: None - could not determine a constructor for the tag '!policy'
secrets.yml:2:17: unparsable-with-libyaml: None - could not determine a constructor for the tag '!var'
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
