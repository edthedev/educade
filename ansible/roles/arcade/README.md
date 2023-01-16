Role Name
=========

Install RetroPie on an Armbian host.

Requirements
------------

Assumes the remote host is Armbian. Raspbian should also work.

Role Variables
--------------

Example Playbook
----------------

```yaml
- name: Setup a new arcade machine
  gather_facts: no
  hosts: arcades
  become: yes
  vars:
    - pi_user: pi

  tasks:
    - name: Add retropie
      include_role:
        name: arcade
```

License
-------

BSD

Author Information
------------------

Copyright 2023 Edward Delaporte
https://edward.delaporte.us
