# Ansible for Recalbox

Add custom systems to RecalBox.

See [RecalBox es_systems.cfg][5] for examples.

[5]: https://github.com/recalbox/recalbox-buildroot/blob/master/board/recalbox/fsoverlay/recalbox/share_init/system/.emulationstation/es_systems.cfg

## Add a `Classics` Collection

```sh
ansible-playbook classics.yml --hosts
```

## TODO:

- Grab example code from my work on McAirpos
- Create a template config that maps a new name to a folder 
- Look into how to do art for the collection main page...
