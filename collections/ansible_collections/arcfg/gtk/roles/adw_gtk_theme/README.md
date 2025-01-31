# Ansible Role "adw_gtk_theme"

> The theme from libadwaita ported to GTK-3

## Resources

### Official

- site: https://github.com/lassekongo83/adw-gtk3
- repo: https://github.com/lassekongo83/adw-gtk3
- docs: https://github.com/lassekongo83/adw-gtk3?tab=readme-ov-file#adw-gtk3

### Additional

-

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
- name: Apply adw-gtk-theme configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.gtk.adw_gtk_theme
```

```yaml
- name: Apply adw-gtk-theme configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.gtk.adw_gtk_theme
      tags:
        - laptop
        - desktop
```
