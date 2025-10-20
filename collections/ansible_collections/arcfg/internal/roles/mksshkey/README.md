# Ansible Role "mksshkey"

> Create SSH keypair

## Requirements

- openssh

## Role Variables

### Global scope

- `git_user_email` - default Git user email

### Role scope

- `item` - SSH host name or host options object:
  - host: target service host
  - alg: key algorithm (optional)
  - size: key size (optional, RSA key type only)
  - email: user email for use with this key (optional)
  - username: username for use with this key (optional)

## Dependencies

Collections:

- name: community.general
- name: community.crypto

## Examples

### Use in tasks

```yaml
# hostvars
git_user_email: "test@example.com"
```

```yaml
# vars/main.yml
ssh_hosts:
  - "github.com"
  - host: "gitlab.com"
    email: "test@email.test"
  - host: "bitbucket.org"
    alg: "rsa"
    size: "4096"
```

```yaml
# tasks/main.yml
- name: Pass variables to role
  ansible.builtin.include_role:
    name: arcfg.internal.mksshkey
  loop: "{{ ssh_hosts }}"
```

### Use in playbook

```yaml
# hostvars
ssh_hosts:
  - "github.com"
  - host: "gitlab.com"
    email: "test@email.test"
  - host: "bitbucket.org"
    alg: "rsa"
    size: "4096"
```

```yaml
- name: Apply mksshkey configuration to local node
  hosts: localhost
  tasks:
    - name: Generate SSH key for localhost
      ansible.builtin.include_role:
        name: arcfg.internal.mksshkey
      loop: "{{ ssh_hosts }}"
```
