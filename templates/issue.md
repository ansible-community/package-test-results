{% set artifact = collection_name.replace(".", "-") ~ "-" ~ tag_output.version ~ ".tar.gz" %}

As per the [Ansible community package inclusion requirements][ci-testing], collections must pass `ansible-test sanity` tests. Version `{{ tag_output.version }}` of `{{ collection_name }}`, corresponding to the `{{ tag_output.tag }}` tag in this repo, fails one or more of the required sanity tests.

{% if file_errors %}
Additionally, the contents in the `{{ tag_output.tag }}` git tag do not match `{{ artifact }}` as uploaded to Ansible Galaxy. For future releases, please make sure that the contents uploaded to Galaxy match the sources that were tagged as that release. See the [Repository management requirements][repo-mgmt] for more information.
{% endif %}

Please see the errors below and address them. If these issues aren't addressed within a reasonable time period, the collection may be subject to [removal from Ansible][removal].

Thank you for your efforts and for being part of the Ansible package! We appreciate it.

---

## Sanity test failures

The following tests were run using `ansible-test` version `{{ env_details.ansible_test_version }}`:

{% for test in env_details.sanity_tests %}
- {{ test }}
{% endfor %}

Note that this is only a subset of the required sanity tests. Please make sure you run them in all in your CI.

### Results

{% for file in test_json.values() %}
{% for result in file.results %}
{{ result.message }}

``` text
{{ result.output }}
```

{% endfor %}
{% endfor %}

{% if file_errors %}
## File divergences

The following files differ between the `{{ tag_output.tag }}` git tag and `{{ artifact }}` on Ansible Galaxy:

{% for file in file_errors %}
- `{{ file.file }}` (`{{ file.error }}`{{ (" : " ~ file.message) if "message" in file else "" }})
{% endfor %}

{% endif %}

[ci-testing]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#ci-testing
[repo-mgmt]: https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_requirements.html#repository-management
[removal]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
