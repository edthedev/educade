
# About

These scripts help maintain my home arcade, most of which runs Armbian.

## Expected Inventory

Add hosts to `/etc/ansible/hosts` before running the playbooks.

Expected intenvory categories:

- `[new]` - for hosts that have not had initial setup performed, such as adding a user to Ansible to use
- `[school]` - hosts that will run XFCE and educational software
- `[arcades]` - hosts that will be installed into a Aracde machine frame
- `[armbian]` - hosts that run Armbian
- `[legacy_arcades]` - hosts installed to an Aracde machine, but running Batocera rather than Armbian

## Playbooks

Run these playbooks with the `ansible-playbook` command.

```sh
ansible-playbook --ask-become-pass new.yml
```

> Either `--ask-become-pass` the first time, or `scp` a public key to the root user.

- `new.yml` - Creates users for reliable access by Ansible.
- `hostname.yml` sets a new hostname on Armbian.
- `retropie_setup.yml` clones the RetroPie setup scripts onto the Armbian computer, defaulting to `/home/pi/RetroPie-Setup/`.

