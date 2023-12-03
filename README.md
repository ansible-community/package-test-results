<!--
Copyright (C) 2023 Maxwell G <maxwell@gtmx.me
SPDX-License-Identifier: GPL-3.0-or-later
-->

# `ansible` Package Test Results

 Coordination for Ansible package-wide testing
 See
 https://forum.ansible.com/t/testing-collections-within-the-ansible-package/2455/.

1. [Data files](https://github.com/ansible-community/package-test-results/tree/main/data/) from `antsibull-build verify-upstreams` (compares Galaxy collection artifacts and git sources) and `antsibull-build sanity-tests` (runs `ansible-test sanity` across collections and combines results)
2. [Script](https://github.com/ansible-community/package-test-results/blob/main/main.py) to generate a report of all of a collection's errors and file an issue.
3.  [Issue Jinja2 template](https://github.com/ansible-community/package-test-results/blob/main/templates/issue.md?plain=1)
4. [Rendered issues](https://github.com/ansible-community/package-test-results/tree/main/examples/rendered) so you can see what this looks like.

## License

    GPL-3.0-or-later
