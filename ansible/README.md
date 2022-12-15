
# Playbooks

## new.yml

Creates our initial access users.

Either `--ask-become-pass` the first time, or `scp` a public key to the root user.

```sh
ansible-playbook --ask-become-pass new.yml
```

## hostname.yml

Sets a new hostname on Armbian.
