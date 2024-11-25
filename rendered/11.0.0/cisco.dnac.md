# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `6.22.0` of `cisco.dnac`, corresponding to the `v6.22.0` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

*Please fix the issues identified below and then create a new Galaxy release so the fixes are caught in the next round of automated testing.*

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.18.0`:

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

The test `ansible-test sanity --test validate-modules` [[explain](https://docs.ansible.com/ansible-core/2.18/dev_guide/testing/sanity/validate-modules.html)] failed with 5 errors:

``` text
plugins/modules/discovery.py:0:0: option-equal-up-to-casing: Multiple options/aliases are equal up to casing: option 'snmpROCommunity', option 'snmpRoCommunity'
plugins/modules/discovery.py:0:0: option-equal-up-to-casing: Multiple options/aliases are equal up to casing: option 'snmpROCommunityDesc', option 'snmpRoCommunityDesc'
plugins/modules/discovery.py:0:0: option-equal-up-to-casing: Multiple options/aliases are equal up to casing: option 'snmpRWCommunity', option 'snmpRwCommunity'
plugins/modules/discovery.py:0:0: option-equal-up-to-casing: Multiple options/aliases are equal up to casing: option 'snmpRWCommunityDesc', option 'snmpRwCommunityDesc'
plugins/modules/discovery.py:0:0: option-equal-up-to-casing: Multiple options/aliases are equal up to casing: option 'timeOut', option 'timeout'
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
