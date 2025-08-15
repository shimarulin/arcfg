# Ansible Role "console"

> Ansible role to prepare color palette to Linux console (kernel parameters)

## Resources

- https://wiki.archlinux.org/title/Color_output_in_console#Virtual_console
- https://wiki.archlinux.org/title/User:Isacdaavid/Linux_Console#Kernel_parameters

## Examples

- https://github.com/catppuccin/base16/blob/main/base16/macchiato.yaml
- https://github.com/catppuccin/tty/blob/main/themes/macchiato.txt

## Description

Linux exposes the default console palette setters as part of
the [parameters](https://wiki.archlinux.org/title/Kernel_parameters "Kernel parameters") that can be passed to it at
boot, therefore appending the following line to your bootloader will have the effect of changing colors from the very
beginning and for all tty's, and is as effective
as [#hard-coding colors at compilation time](https://wiki.archlinux.org/title/User:Isacdaavid/Linux_Console#Recompiling_the_kernel).
The format is _vt.default_red=[color_0_red_component],[color_1_red_component],...,[color_15_red_component]
vt.default_grn=[color_0_green_component],[color_1_green_component],...,[color_15_green_component]
vt.default_blu=[color_0_blue_component],[color_1_blue_component],...,[color_15_blue_component]_.

For a completely blank screen:

```
vt.default_red=0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00 vt.default_grn=0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00 vt.default_blu=0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
```

Refer to [kernel parameters](https://wiki.archlinux.org/title/Kernel_parameters "Kernel parameters") to know where to
add this line.

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
- name: Apply console configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.themes.console
```

```yaml
- name: Apply console configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.themes.console
      tags:
        - laptop
        - desktop
```
