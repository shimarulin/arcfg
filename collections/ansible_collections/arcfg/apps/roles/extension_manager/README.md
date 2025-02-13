# Ansible Role "extension_manager"

> A utility for browsing and installing GNOME Shell Extensions

## Resources

### Official

- site: https://mattjakeman.com/apps/extension-manager
- repo: https://github.com/mjakeman/extension-manager
- docs: https://github.com/mjakeman/extension-manager?tab=readme-ov-file

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
- name: Apply extension-manager configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.apps.extension_manager
```

```yaml
- name: Apply extension-manager configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.apps.extension_manager
      tags:
        - laptop
        - desktop
```
