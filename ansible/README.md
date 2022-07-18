# Ansible for Recalbox

Adds custom systems to RecalBox.
Each system is simply another menu item for an existing system, i.e. 'Megadrive Co-Op'. Add your ROMS to that folder to have them appear under that system.

See [RecalBox es_systems.cfg][5] for examples.

[5]: https://github.com/recalbox/recalbox-buildroot/blob/master/board/recalbox/fsoverlay/recalbox/share_init/system/.emulationstation/es_systems.cfg

## Add my custom collections

Example command:

```sh
ansible-playbook -i "tmntcade.local," --user "root" ./my_collections.yml
```

## TODO:

- [ ] Look into how to do art for the collection main page...
