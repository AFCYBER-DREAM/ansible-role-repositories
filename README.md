ansible-role-repositories
=========

[![Build Status](https://travis-ci.org/AFCYBER-DREAM/ansible-role-repositories.svg?branch=master)](https://travis-ci.org/AFCYBER-DREAM/ansible-role-repositories)

Ansible role to install repositories defined by variables

Using this role
--------------

The role needs to be loaded dynamically during the plays and the dictionary of parameters to pass to the role.

Role Variables
--------------

This role will need to be provided with a dictionary of variables that define the repositories to be installed
It can either be a RPM based package or a dictionary of the variables need to be set 

```
namespace_repositories:
  redhat:
    - { url: "https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm" }
    - { name: "ius",
        description: "IUS Community Packages for Enterprise Linux 7",
        baseurl: "https://dl.iuscommunity.org/pub/ius/stable/CentOS/7/$basearch",
        enabled: 1,
        gpgcheck: 0,
        gpgkey: "file:///etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY" }
```

Example Playbook
----------------

Example import:
```
...
- import_role:
    name: ansible-role-repositories
  vars:
    packages: "{{ namespace_repositories }}"
...
```
License
-------

MIT

Author Information
------------------
The Development Range Engineering, Architecture, and Modernization (DREAM) Team