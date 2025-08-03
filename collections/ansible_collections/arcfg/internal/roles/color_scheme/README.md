# Ansible Role "color_scheme"

> Set color scheme to Ansible facts

## Resources

### Gogh

- site: https://gogh-co.github.io/Gogh/
- repo: https://github.com/Gogh-Co/Gogh
- docs: https://github.com/Gogh-Co/Gogh

### Additional themes

- https://nvchad.com/themes/
- https://github.com/NvChad/base46/blob/v3.0/lua/base46/themes/aquarium.lua
- https://github.com/chriskempson/base16-schemes-source
- https://github.com/chriskempson/base16-unclaimed-schemes
- https://github.com/kovidgoyal/kitty-themes
- https://github.com/kepano/flexoki
- https://github.com/lemnos/theme.sh/tree/master/themes
- https://github.com/catppuccin
- https://github.com/dracula/dracula-theme
- https://github.com/romainl/Apprentice
- https://github.com/Binaryify/OneDark-Pro
- https://github.com/tokyo-night/tokyo-night-vscode-theme
- https://github.com/chriskempson/tomorrow-theme

### Tools

- https://github.com/chriskempson/base16
- https://github.com/lemnos/theme.sh
- https://github.com/stayradiated/terminal.sexy

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
- name: Apply color_scheme configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.internal.color_scheme
```

```yaml
- name: Apply color_scheme configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.internal.color_scheme
      tags:
        - laptop
        - desktop
```
