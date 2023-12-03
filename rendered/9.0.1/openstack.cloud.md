# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `2.1.0` of `openstack.cloud`, corresponding to the `2.1.0` tag in this repo, fails one or more of the required sanity tests.


Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity tests

The following tests were run using `ansible-test` version `2.16.0`:

- ansible-doc
- compile
- validate-modules
- yamllint

Note that this is only a subset of the required sanity tests. Please make sure you run them in all in your CI.

### Results

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 4 errors:

``` text
plugins/modules/compute_flavor.py:252:14: SyntaxError: **self._build_update_extra_specs(flavor),
plugins/modules/loadbalancer.py:387:18: SyntaxError: return {**update, **floating_ip_update}, floating_ip
plugins/modules/security_group.py:305:14: SyntaxError: **self._build_update_security_group(security_group),
plugins/modules/server.py:891:14: SyntaxError: **self._build_update_ips(server),
```

The test `ansible-test sanity --test yamllint` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/yamllint.html)] failed with 2 errors:

``` text
.zuul.yaml:296:14: unparsable-with-libyaml: None - could not determine a constructor for the tag '!encrypted/pkcs1-oaep'
ci/roles/server_group/defaults/main.yml:11:1: empty-lines: too many blank lines (1 > 0)
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
