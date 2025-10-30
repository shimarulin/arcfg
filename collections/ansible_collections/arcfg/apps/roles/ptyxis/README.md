# Ansible Role "ptyxis"

> Container-Oriented Terminal for GNOME

## Resources

### Official

- site: https://flathub.org/en/apps/app.devsuite.Ptyxis
- repo: https://gitlab.gnome.org/chergert/ptyxis/
- docs: https://gitlab.gnome.org/chergert/ptyxis/#ptyxis-your-container-oriented-terminal-for-gnome

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
- name: Apply ptyxis configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.apps.ptyxis
```

```yaml
- name: Apply ptyxis configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.apps.ptyxis
      tags:
        - laptop
        - desktop
```
