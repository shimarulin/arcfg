# Ansible Role "nautilus"

> A file browser for GNOME

## Resources

### Official

- site: https://apps.gnome.org/ru/Nautilus/
- repo: https://gitlab.gnome.org/GNOME/nautilus
- docs: https://gnome.pages.gitlab.gnome.org/nautilus/

### Additional

- https://wiki.archlinux.org/title/GNOME/Files

## Scripts

- https://github.com/cfgnunes/nautilus-scripts
- https://github.com/roman-yagodin/nautilus-scripts
-

### Articles

- https://linuxconfig.org/how-to-extend-the-gnome-nautilus-file-manager-with-custom-scripts

## Extensions

- https://gitlab.gnome.org/philippun1/turtle/
- https://github.com/chr314/nautilus-copy-path
- https://github.com/alt-gnome/nautilus-backspace
- https://github.com/realmazharhussain/nautilus-code

### Extensions development

- https://gnome.pages.gitlab.gnome.org/nautilus-python/
- https://gitlab.gnome.org/madmurphy/nextgen
- https://linuxconfig.org/how-to-write-nautilus-extensions-with-nautilus-python
- https://thelinuxcode.com/python-os-system/

### References

- https://github.com/Stunkymonkey/nautilus-open-any-terminal
- https://github.com/gnunn1/tilix/blob/master/data/nautilus/open-tilix.py
- https://github.com/KaspianDev/kaspian-kitty-nautilus/blob/main/kitty-nautilus.py
- https://github.com/alt-gnome/nautilus-backspace/blob/main/Back.py
- https://github.com/ppvan/nautilus-open-in-blackbox
- https://github.com/nautilus-extensions/open-in-tilix
- https://github.com/madmurphy/nautilus-launch
- https://github.com/i-am-g2/Nautilus-VSCode?tab=readme-ov-file
- https://github.com/bassmanitram/actions-for-nautilus?tab=readme-ov-file#configuration-ui

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the
role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

A description of the settable variables for this role should go here, including any variables that are in
defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables
that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as
well.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set
for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for
users too:

```yaml
- name: Apply nautilus configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.apps.nautilus
```

```yaml
- name: Apply nautilus configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.apps.nautilus
      tags:
        - laptop
        - desktop
```
