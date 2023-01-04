
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

> Add hosts to these inventories when you get a 'no matching hosts found' message from a Playbook.

## Playbooks

Run these playbooks with the `ansible-playbook` command.

```sh
ansible-playbook new.yml
```

> Tip: `new.yml` will prompt for username and password to use to connect.

### For New Armbian Hosts

- `new.yml` - Creates users for reliable access by Ansible.
- `hostname.yml` sets a new hostname on Armbian.

> Tip: Be sure to add the host IP to [new] in `/etc/ansible/hosts`.

> Tip: Run `armbian-config` to enable auto-login, and disable `ssh` root user.

### More playbooks

- `retropie_setup.yml` clones the RetroPie setup scripts onto the Armbian computer, defaulting to `/home/pi/RetroPie-Setup/`.


