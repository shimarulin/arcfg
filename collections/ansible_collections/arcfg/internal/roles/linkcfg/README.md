# Ansible Role "linkcfg"

> Ansible role to backup existing config files and create symbolic links to config dirs

## Role Variables

- `src`: The absolute path to the source configuration file or directory to be linked
- `dest`: The absolute path to the target location of the configuration file or directory
- `mode`: The permissions of the destination file or directory

## Usage

```yaml
# NOTE: workaround to keep current role path
- name: "Set current role path"
  ansible.builtin.set_fact:
    zsh_role_path: "{{ role_path }}"

- name: "Create a symbolic links to zsh config dirs"
  ansible.builtin.include_role:
    name: "arcfg.internal.linkcfg"
  vars:
    linkcfg_items:
      - src: "{{ zsh_role_path }}/files/home/user/.config/sheldon"
        dest: "{{ ansible_user_dir }}/.config/sheldon"
        mode: "u=rwx,g=rx,o=rx"
      - src: "{{ zsh_role_path }}/files/home/user/.config/starship"
        dest: "{{ ansible_user_dir }}/.config/starship"
        mode: "u=rwx,g=rx,o=rx"
      - src: "{{ zsh_role_path }}/files/home/user/.config/zsh"
        dest: "{{ ansible_user_dir }}/.config/zsh"
        mode: "u=rwx,g=rx,o=rx"
      - src: "{{ zsh_role_path }}/files/home/user/.zshenv"
        dest: "{{ ansible_user_dir }}/.zshenv"
        mode: "u=rw,g=r,o=r"
```
