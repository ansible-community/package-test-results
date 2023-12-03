# Community package requirements: sanity tests

(Note: This issue was filed in a semi-automated fashion. Let me know if you see errors in this issue.)

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `8.4.0` of `dellemc.openmanage`, corresponding to the `v8.4.0` tag in this repo, fails one or more of the required sanity tests.


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

The test `ansible-test sanity --test compile --python 2.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 6 errors:

``` text
plugins/modules/idrac_network_attributes.py:649:34: SyntaxError: if (job_tracking_uri := job_resp.headers.get("Location")):
plugins/modules/ome_alert_policies.py:566:74: SyntaxError: query_param = {"$filter": f"{filter_param} eq '{item_id}'"}
plugins/modules/ome_alert_policies_info.py:147:24: SyntaxError: def __init__(self) -> None:
plugins/modules/ome_job_info.py:324:19: SyntaxError: if value := json_data.get('value'):
tests/unit/plugins/modules/test_idrac_network_attributes.py:991:64: SyntaxError: 'clear_pending': True if exec == 'URLError' else False})
tests/unit/plugins/modules/test_ome_alert_policies.py:1545:64: SyntaxError: with open(f"{params['mparams'].get('message_file')}", 'w', encoding='utf-8') as fp:
```

The test `ansible-test sanity --test compile --python 3.6` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 2 errors:

``` text
plugins/modules/idrac_network_attributes.py:649:34: SyntaxError: if (job_tracking_uri := job_resp.headers.get("Location")):
plugins/modules/ome_job_info.py:324:19: SyntaxError: if value := json_data.get('value'):
```

The test `ansible-test sanity --test compile --python 3.7` [[explain](https://docs.ansible.com/ansible-core/2.16/dev_guide/testing/sanity/compile.html)] failed with 2 errors:

``` text
plugins/modules/idrac_network_attributes.py:649:34: SyntaxError: if (job_tracking_uri := job_resp.headers.get("Location")):
plugins/modules/ome_job_info.py:324:19: SyntaxError: if value := json_data.get('value'):
```




[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
