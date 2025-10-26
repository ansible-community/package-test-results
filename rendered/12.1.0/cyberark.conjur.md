# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion on behalf of the Ansible Community Steering Committee. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `1.3.7` of `cyberark.conjur`, corresponding to the `v1.3.7` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.19/dev_guide/testing/sanity/yamllint.html)] failed with 23 errors:

``` text
dev/policy/cloud/api_key/root.yml:2:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/azure/authn-azure-AzureAnsible.yml:4:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/azure/authn-azure-hosts.template.yml:6:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/azure/authn-azure-permission.yml:3:3: unparsable-with-libyaml: could not determine a constructor for the tag '!grant'
dev/policy/cloud/azure/authn-azure-secrets.yml:4:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/gcp/authn-gcp-hosts.template.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/gcp/authn-gcp-permission.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!grant'
dev/policy/cloud/gcp/authn-gcp-secrets.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/gcp/authn-gcp.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!webservice'
dev/policy/cloud/iam/authn-iam-host.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/iam/authn-iam.yml:2:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/cloud/iam/authn-iam.yml:13:1: empty-lines: too many blank lines (1 > 0)
dev/policy/cloud/iam/authn-permission.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!grant'
dev/policy/oss_ent/api_key/root.yml:2:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/azure/authn-azure-AzureWS.yml:4:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/azure/authn-azure-hosts.template.yml:6:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/azure/authn-azure-secrets.yml:4:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/gcp/authn-gcp-hosts.template.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/gcp/authn-gcp-secrets.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/gcp/authn-gcp.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/iam/authn-iam-host.yml:1:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/iam/authn-iam.yml:2:3: unparsable-with-libyaml: could not determine a constructor for the tag '!policy'
dev/policy/oss_ent/iam/authn-iam.yml:13:1: empty-lines: too many blank lines (1 > 0)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
