# arcfg

> My own Ansible managed Arch Linux configuration

## Requirements

```sh
sudo pacman -S git python-uv
```

## Installation

```sh
git clone git@github.com:shimarulin/arcfg.git ~/.local/share/arcfg
cd ~/.local/share/arcfg
uv sync --group dev
uv run ansible-galaxy collection install -r ./collections/requirements.yml
```

## Usage

### Setup variables

```sh
uv run mkvars
```

### Run playbook

```sh
uv run ansible-playbook arcfg.gnome.main
```

### Output a playbook stdout to the log file

```sh
uv run ansible-playbook arcfg.desktop.tty > .logs/play/arcfg.desktop.tty__$(date +"%Y-%m-%d_%T").log
```

## Development

```sh
uv run pre-commit install --install-hooks
```

### Create new role

```sh
uv run mkrole
```

By default, this command implies installing a package with a name matching the name of the role being created.

### Mount project to virtual instance (QEMU/KVM)

#### Host system

VM virtual fs settings example:

```xml
<filesystem type="mount" accessmode="passthrough">
  <driver type="virtiofs"/>
  <binary path="/usr/lib/virtiofsd"/>
  <source dir="/home/username/.local/share/arcfg"/>
  <target dir="arcfg"/>
  <alias name="fs0"/>
  <address type="pci" domain="0x0000" bus="0x09" slot="0x00" function="0x0"/>
</filesystem>
```

#### Virtual machine

Create on VM mount point:

```sh
mkdir -p ~/.local/share/arcfg
```

Automount virtual fs with `/etc/fstab`:

```
arcfg    /home/vagrant/.local/share/arcfg    virtiofs    defaults    0 0
```

Create an additional environment configuration file manually:

```sh
echo 'export UV_PROJECT_ENVIRONMENT=${HOME}/.local/share/arcfg/.cache/vmvenv' | sudo tee -a /etc/profile.d/00-arcfg.sh
```

or use a script after reboot:

```sh
cd ~/.local/share/arcfg && ./vm-init
```

Reboot, jump to `~/.local/share/arcfg` dir and reinstall packages

```sh
uv sync --group dev
```

### Watch DConf changes

```shell
dconf watch / > .logs/dconf.log
```
