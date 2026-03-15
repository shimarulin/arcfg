## 6. Автоматизация через Ansible

### Структура роли

```
roles/vscode/
├── defaults/
│   └── main.yml
├── vars/
│   └── main.yml
├── tasks/
│   ├── main.yml
│   ├── install.yml
│   ├── configure_base.yml
│   ├── configure_profiles.yml
│   └── extensions.yml
├── templates/
│   ├── settings_base.json.j2
│   └── settings_profile.json.j2
└── files/
    └── vscode-config/
        ├── base/
        │   └── keybindings.json
        └── profiles/
            ├── python/
            │   └── settings.json
            ├── web/
            │   └── settings.json
            └── devops/
                └── settings.json
```

### defaults/main.yml

```yaml
# Какие профили создавать на данном хосте
vscode_profiles_enabled:
  - web
  - python
  - devops

# Пользователь
vscode_user: "{{ ansible_user_id }}"
vscode_user_home: "{{ ansible_env.HOME }}"

# Пути (автоопределение по ОС)
vscode_config_dir: >-
  {% if ansible_os_family == 'Darwin' %}
  {{ vscode_user_home }}/Library/Application Support/Code/User
  {% elif ansible_os_family == 'Windows' %}
  {{ ansible_env.APPDATA }}/Code/User
  {% else %}
  {{ vscode_user_home }}/.config/Code/User
  {% endif %}

# Команда VS Code
vscode_bin: "code"

# ===== Базовые расширения (устанавливаются всегда) =====
vscode_base_extensions:
  # Тема
  # - zhuangtongfa.material-theme
  # - pkief.material-icon-theme
  # Git
  - eamodio.gitlens
  # Инструменты
  - editorconfig.editorconfig
  # - streetsidesoftware.code-spell-checker
  # - usernamehw.errorlens
  # - gruntfuggly.todo-tree
  # - christian-kohler.path-intellisense
  # - redhat.vscode-yaml
  # - tamasfe.even-better-toml
  # - mechatroner.rainbow-csv
  # Remote
  # - ms-vscode-remote.remote-ssh
  # - ms-vscode-remote.remote-containers

# ===== Настройки, наследуемые всеми профилями =====
# Эти ключи попадут в workbench.settings.applyToAllProfiles
vscode_inherited_settings_keys:
  # Окно
  "window.titleBarStyle"
  "window.commandCenter"
  "window.menuBarVisibility"
  "window.customTitleBarVisibility"
  # Редактор
  - "editor.fontSize"
  - "editor.fontFamily"
  # - "editor.fontLigatures"
  # - "editor.tabSize"
  # - "editor.insertSpaces"
  # - "editor.wordWrap"
  # - "editor.minimap.enabled"
  # - "editor.renderWhitespace"
  # - "editor.bracketPairColorization.enabled"
  # - "editor.guides.bracketPairs"
  # - "editor.suggestSelection"
  # - "editor.formatOnSave"
  # - "editor.formatOnPaste"
  # - "editor.linkedEditing"
  # - "editor.stickyScroll.enabled"
  # - "editor.cursorBlinking"
  # - "editor.cursorSmoothCaretAnimation"
  # - "editor.smoothScrolling"
  # Терминал
  - "terminal.integrated.fontSize"
  - "terminal.integrated.fontFamily"
  # - "terminal.integrated.cursorStyle"
  - "terminal.integrated.scrollback"
  # Файлы
  - "files.trimTrailingWhitespace"
  - "files.insertFinalNewline"
  - "files.trimFinalNewlines"
  - "files.autoSave"
  # - "files.autoSaveDelay"
  - "files.exclude"
  # Рабочая область
  # - "workbench.startupEditor"
  # - "workbench.colorTheme"
  # - "workbench.iconTheme"
  # - "workbench.tree.indent"
  # - "workbench.editor.enablePreview"
  # Проводник
  "explorer.confirmPasteNative",
  # Поиск
  - "search.exclude"
  # Git
  - "git.autofetch"
  - "git.confirmSync"
  # - "git.enableSmartCommit"
  # Телеметрия
  - "telemetry.telemetryLevel"
  - "extensions.autoUpdate"

# ===== Базовые настройки (значения) =====
vscode_base_settings:
  # Окно
  window.titleBarStyle: "custom"
  window.commandCenter: true
  window.menuBarVisibility: "visible"
  window.customTitleBarVisibility: "auto"
  # Редактор
  editor.fontSize: 14
  editor.fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
  # editor.fontLigatures: true
  # editor.tabSize: 4
  # editor.insertSpaces: true
  # editor.wordWrap: "on"
  # editor.minimap.enabled: false
  # editor.renderWhitespace: "boundary"
  # editor.bracketPairColorization.enabled: true
  # editor.guides.bracketPairs: "active"
  # editor.suggestSelection: "first"
  # editor.formatOnSave: true
  # editor.formatOnPaste: false
  # editor.linkedEditing: true
  # editor.stickyScroll.enabled: true
  # editor.cursorBlinking: "smooth"
  # editor.cursorSmoothCaretAnimation: "on"
  # editor.smoothScrolling: true
  # Терминал
  terminal.integrated.fontSize: 13
  terminal.integrated.fontFamily: "'JetBrains Mono'"
  terminal.integrated.cursorStyle: "line"
  terminal.integrated.scrollback: 10000
  # Файлы
  files.trimTrailingWhitespace: true
  files.insertFinalNewline: true
  files.trimFinalNewlines: true
  files.autoSave: "afterDelay"
  files.autoSaveDelay: 1000
  files.exclude:
    "**/.git": true
    "**/.DS_Store": true
    "**/__pycache__": true
    "**/.pytest_cache": true
    "**/node_modules": true
    "**/*.pyc": true
  # Проводник
  explorer.confirmPasteNative: false
  # Рабочая область
  workbench.startupEditor: "none"
  workbench.colorTheme: "One Dark Pro"
  workbench.iconTheme: "material-icon-theme"
  workbench.tree.indent: 16
  workbench.editor.enablePreview: false
  # Поиск
  search.exclude:
    "**/node_modules": true
    "**/dist": true
    "**/.git": true
    "**/coverage": true
  # Git
  git.autofetch: true
  git.confirmSync: false
  git.enableSmartCommit: true
  # Телеметрия
  telemetry.telemetryLevel: "off"
  extensions.autoUpdate: true

# ===== Профили =====
vscode_profile_configs:
  web:
    name: "Web Dev"
    extensions:
      - dbaeumer.vscode-eslint

  python:
    name: "Python Dev"
    extensions:
      - ms-python.python
      # - ms-python.vscode-pylance
      # - ms-python.debugpy
      # - ms-python.vscode-python-envs

      # - charliermarsh.ruff
      # - ms-toolsai.jupyter
      # - ms-toolsai.jupyter-keymap
      # - ms-toolsai.jupyter-renderers
      # - njpwerner.autodocstring
      # - kevinrose.vsc-python-indent

  devops:
    name: "DevOps"
    extensions:
      - redhat.ansible
      - samuelcolvin.jinjahtml
      - redhat.vscode-yaml
      - tamasfe.even-better-toml
      # - ms-azuretools.vscode-docker
      # - ms-kubernetes-tools.vscode-kubernetes-tools
      # - hashicorp.terraform
      # - foxundermoon.shell-format
      # - timonwong.shellcheck
```

### tasks/main.yml

```yaml
---
# tasks file for "arcfg.apps.vscode" role
- name: "Install dependencies"
  become: true
  become_user: "aur_builder"
  kewlfft.aur.aur:
    name: "{{ vscode_packages }}"
    use: "paru"
  # Avoid use local Python venv
  environment:
    PATH: "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl"

- name: Include base configuration
  ansible.builtin.include_tasks: configure_base.yml
  tags: [vscode, vscode-config]

- name: Include profile configuration
  ansible.builtin.include_tasks: configure_profiles.yml
  tags: [vscode, vscode-profiles]
```

### tasks/configure_base.yml

```yaml
- name: Ensure VS Code config directory exists
  ansible.builtin.file:
    path: "{{ vscode_config_dir | trim }}"
    state: directory
    owner: "{{ vscode_user }}"
    mode: "0755"

# Записываем базовые настройки с workbench.settings.applyToAllProfiles.
# Шаблон автоматически включает массив наследуемых ключей.
- name: Write base settings.json with applyToAllProfiles
  ansible.builtin.template:
    src: settings_base.json.j2
    dest: "{{ vscode_config_dir | trim }}/settings.json"
    owner: "{{ vscode_user }}"
    mode: "0644"
    backup: true

- name: Copy base keybindings.json
  ansible.builtin.copy:
    src: vscode-config/base/keybindings.json
    dest: "{{ vscode_config_dir | trim }}/keybindings.json"
    owner: "{{ vscode_user }}"
    mode: "0644"
  when: >
    lookup('first_found',
      dict(files=['files/vscode-config/base/keybindings.json'], skip=true)
    ) | length > 0

- name: Install base extensions
  ansible.builtin.command:
    cmd: "{{ vscode_bin }} --install-extension {{ item }} --force"
  loop: "{{ vscode_base_extensions }}"
  register: ext_result
  changed_when: "'was successfully installed' in ext_result.stdout"
  failed_when: false
  become: true
  become_user: "{{ vscode_user }}"
```

### tasks/configure_profiles.yml

```yaml
- name: Configure VS Code profiles
  ansible.builtin.include_tasks: single_profile.yml
  loop: "{{ vscode_profiles_enabled }}"
  loop_control:
    loop_var: profile_key
  when: profile_key in vscode_profile_configs
```

### tasks/single_profile.yml

Это **ключевой файл**, радикально упрощённый благодаря `applyToAllProfiles` — больше не нужен merge JSON и запись в
SQLite:

```yaml
- name: "Set profile variables for {{ profile_key }}"
  ansible.builtin.set_fact:
    current_profile: "{{ vscode_profile_configs[profile_key] }}"
    current_profile_name: "{{ vscode_profile_configs[profile_key].name }}"

# --- Создание профиля через CLI ---
# VS Code создаёт профиль при первом использовании --profile.
# Устанавливаем фиктивное расширение, чтобы профиль инициализировался.
- name: "Create profile '{{ current_profile_name }}' by installing first extension"
  ansible.builtin.command:
    cmd: >-
      {{ vscode_bin }}
      --profile '{{ current_profile_name }}'
      --install-extension {{ current_profile.extensions[0] }}
      --force
  register: profile_init_result
  changed_when: "'was successfully installed' in profile_init_result.stdout"
  failed_when: false
  become: true
  become_user: "{{ vscode_user }}"
  when: current_profile.extensions | length > 0

# --- Записываем ТОЛЬКО уникальные настройки профиля ---
# Базовые настройки НЕ дублируются — они наследуются автоматически
# через workbench.settings.applyToAllProfiles из Default Profile.
- name: "Find profile directory for {{ current_profile_name }}"
  ansible.builtin.script:
    cmd: |
      #!/usr/bin/env python3
      import sqlite3, json, os, sys
      config_dir = "{{ vscode_config_dir | trim }}"
      db_path = os.path.join(config_dir, "globalStorage", "state.vscdb")
      profile_name = "{{ current_profile_name }}"
      if not os.path.exists(db_path):
          print("NOT_FOUND")
          sys.exit(0)
      conn = sqlite3.connect(db_path)
      cursor = conn.execute(
          "SELECT value FROM ItemTable WHERE key='userDataProfiles'"
      )
      row = cursor.fetchone()
      if row:
          for p in json.loads(row[0]):
              if p.get('name') == profile_name:
                  loc = p['location']
                  print(os.path.join(config_dir, "profiles", loc))
                  sys.exit(0)
      print("NOT_FOUND")
    executable: python3
  register: profile_dir_result
  become: true
  become_user: "{{ vscode_user }}"

- name: "Set profile directory fact for {{ current_profile_name }}"
  ansible.builtin.set_fact:
    profile_dir: "{{ profile_dir_result.stdout | trim }}"
  when: profile_dir_result.stdout | trim != "NOT_FOUND"

# Записываем только профильные настройки (без базовых!)
- name: "Write profile-only settings for {{ current_profile_name }}"
  ansible.builtin.copy:
    src: "vscode-config/profiles/{{ profile_key }}/settings.json"
    dest: "{{ profile_dir }}/settings.json"
    owner: "{{ vscode_user }}"
    mode: "0644"
  when:
    - profile_dir is defined
    - profile_dir != "NOT_FOUND"
    - lookup('first_found',
        dict(files=['files/vscode-config/profiles/' + profile_key + '/settings.json'],
             skip=true)) | length > 0

# --- Устанавливаем базовые расширения в профиль ---
- name: "Install base extensions for profile {{ current_profile_name }}"
  ansible.builtin.command:
    cmd: >-
      {{ vscode_bin }}
      --profile '{{ current_profile_name }}'
      --install-extension {{ item }}
      --force
  loop: "{{ vscode_base_extensions }}"
  register: ext_result
  changed_when: "'was successfully installed' in ext_result.stdout"
  failed_when: false
  become: true
  become_user: "{{ vscode_user }}"

# --- Устанавливаем профильные расширения ---
- name: "Install profile extensions for {{ current_profile_name }}"
  ansible.builtin.command:
    cmd: >-
      {{ vscode_bin }}
      --profile '{{ current_profile_name }}'
      --install-extension {{ item }}
      --force
  loop: "{{ current_profile.extensions }}"
  register: ext_result
  changed_when: "'was successfully installed' in ext_result.stdout"
  failed_when: false
  become: true
  become_user: "{{ vscode_user }}"
```

### templates/settings_base.json.j2

```jinja2
{
    "workbench.settings.applyToAllProfiles": {{ vscode_inherited_settings_keys | to_nice_json(indent=8) }},
{% for key, value in vscode_base_settings.items() %}
    {{ key | to_json }}: {{ value | to_json }}{% if not loop.last %},{% endif %}

{% endfor %}
}
```

### templates/settings_profile.json.j2

```jinja2
{# Этот шаблон используется ТОЛЬКО если профильные настройки
   определены как Ansible-переменные, а не как файлы.
   Записывает ТОЛЬКО уникальные настройки профиля. #}
{{ profile_settings | to_nice_json }}
```

### Playbook для запуска

```yaml
# playbooks/setup_workstation.yml
- name: Setup developer workstation
  hosts: workstations
  become: false

  vars:
    vscode_profiles_enabled:
      - python
      - web
      - devops

  roles:
    - role: vscode
      tags: [vscode]
```

### Inventory с переопределениями

```yaml
# inventory/host_vars/dev-machine-01.yml
vscode_profiles_enabled:
  - python
  - devops

# Переопределяем базовые настройки для этого хоста
vscode_base_settings:
  editor.fontSize: 16
  editor.fontFamily: "'Fira Code', monospace"
  # ... остальные наследуются из defaults
```

```yaml
# inventory/group_vars/frontend_devs.yml
vscode_profiles_enabled:
  - web

vscode_base_settings:
  editor.tabSize: 2
```

### Запуск

```bash
# Полная установка
ansible-playbook playbooks/setup_workstation.yml

# Только конфигурация (без установки)
ansible-playbook playbooks/setup_workstation.yml --tags vscode-config

# Только профили
ansible-playbook playbooks/setup_workstation.yml --tags vscode-profiles

# Конкретный хост
ansible-playbook playbooks/setup_workstation.yml --limit dev-machine-01

# Dry run
ansible-playbook playbooks/setup_workstation.yml --check --diff
```
