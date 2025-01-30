# Ansible Role "bring_out_submenu_of_power_offlogout_button"

> Bring Out Submenu Of Power Off Button

## Resources

### Official

- site: https://extensions.gnome.org/extension/2917/bring-out-submenu-of-power-offlogout-button/
- repo: https://github.com/PRATAP-KUMAR/gse-bring-out-submenu-of-power-off-logout
- docs:
  https://github.com/PRATAP-KUMAR/gse-bring-out-submenu-of-power-off-logout?tab=readme-ov-file#bringout-submenu-extension---gnome-shell-extension

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
- name: Apply bring-out-submenu-of-power-offlogout-button configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.gnome_shell_extensions.bring_out_submenu_of_power_offlogout_button
```

```yaml
- name: Apply bring-out-submenu-of-power-offlogout-button configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.gnome_shell_extensions.bring_out_submenu_of_power_offlogout_button
      tags:
        - laptop
        - desktop
```
