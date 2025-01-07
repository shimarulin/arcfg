# arcfg

> My own Ansible managed Arch Linux configuration

## Requirements

```sh
sudo pacman -S python-uv
```

## Installation

```sh
git clone git@github.com:shimarulin/arcfg.git ~/.local/share/arcfg
cd ~/.local/share/arcfg
uv sync --group dev
uv run ansible-galaxy collection install -r ./collections/requirements.yml
uv run pre-commit install --install-hooks
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

### Create new role

```sh
uv run mkvars
```

By default, this command implies installing a package with a name matching the name of the role being created.
