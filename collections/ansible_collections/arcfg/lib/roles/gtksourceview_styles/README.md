# Ansible Role "gtksourceview_styles"

> GtkSourceView style schemes

## Resources

### Official

- site: https://wiki.gnome.org/Projects/GtkSourceView/StyleSchemes
- repo: https://gitlab.gnome.org/GNOME/gtksourceview/-/tree/master/data/styles
- docs: https://gnome.pages.gitlab.gnome.org/gtksourceview/gtksourceview5/

### Install styles

Either copy your files to

```bash
~/.local/share/gtksourceview-3.0/styles/
```

or for gtksourceview 4 to

```bash
~/.local/share/gtksourceview-4/styles/
```

or for gtksourceview 5 to

```bash
~/.local/share/gtksourceview-5/styles/
```

### Themes

- https://github.com/nordtheme/gedit
- https://github.com/catppuccin/gedit
- https://github.com/dracula/gedit
- https://github.com/Fausto-Korpsvart/Nightfox-GTK-Theme/blob/main/extra/text-editor/nightfox-dusk.xml
- https://github.com/Fausto-Korpsvart/Tokyonight-GTK-Theme/tree/master/extra/text-editor
- https://github.com/Fausto-Korpsvart/Catppuccin-GTK-Theme/tree/main/extra/text-editor

#### Abandoned

- https://github.com/Peter-van-der-Velde/Two-Dark
- https://github.com/isdampe/gedit-gtk-one-dark-style-scheme

### Color palette

- https://github.com/pineapplegiant/spaceduck
- https://cocopon.github.io/iceberg.vim/

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
- name: Apply gtksourceview-styles configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.lib.gtksourceview_styles
```

```yaml
- name: Apply gtksourceview-styles configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.lib.gtksourceview_styles
      tags:
        - laptop
        - desktop
```
