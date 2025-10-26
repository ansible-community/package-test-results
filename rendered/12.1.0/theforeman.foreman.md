# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `5.6.0` of `theforeman.foreman`, corresponding to the `v5.6.0` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/yamllint.html)] failed with 107 errors:

``` text
tests/test_playbooks/fixtures/auth_source_ldap-0.yml:302:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/auth_source_ldap-1.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/auth_source_ldap-2.yml:382:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/auth_source_ldap-3.yml:382:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/auth_source_ldap-4.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/auth_source_ldap-5.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/auth_source_ldap-6.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-0.yml:6276:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-1.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-2.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-3.yml:107:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-4.yml:107:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-5.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/bookmark-6.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/compute_attribute-0.yml:151:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/compute_attribute-1.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/compute_attribute-2.yml:154:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/compute_attribute-3.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-0.yml:225:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-1.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-2.yml:308:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-3.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-4.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-5.yml:225:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-6.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_credential-7.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-0.yml:381:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-1.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-2.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-3.yml:385:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-4.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-5.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-6.yml:937:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-7.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-8.yml:1087:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/content_view_version-9.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-0.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-1.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-2.yml:104:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-3.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-4.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-5.yml:104:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-6.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/host_power-7.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-0.yml:257:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-1.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-10.yml:498:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-11.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-12.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-13.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-2.yml:258:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-3.yml:261:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-4.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-5.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-6.yml:220:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-7.yml:261:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-8.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/installation_medium-9.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-0.yml:302:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-1.yml:17:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-10.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-11.yml:2988:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-12.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-13.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-2.yml:398:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-3.yml:332:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-4.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-5.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-6.yml:264:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-7.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-8.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/job_template-9.yml:197:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-0.yml:431:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-1.yml:433:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-2.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-3.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-4.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-5.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-6.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/os_default_template-7.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/realm-0.yml:110:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/realm-1.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/realm-2.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/realm-3.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-0.yml:110:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-1.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-2.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-3.yml:111:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-4.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-5.yml:115:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-6.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-7.yml:111:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-8.yml:9:20: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/setting-9.yml:111:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-0.yml:120:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-1.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-10.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-11.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-12.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-2.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-3.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-4.yml:120:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-5.yml:180:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-6.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-7.yml:11:15: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-8.yml:120:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
tests/test_playbooks/fixtures/usergroup-9.yml:428:11: unparsable-with-libyaml: could not determine a constructor for the tag 'tag:yaml.org,2002:python/unicode'
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
