# Ansible Role "niri_lisgd"

> Run niri action by lisgd gestures

## 1. Скрипт определения устройства (`~/.local/bin/niri-lisgd-device-setup`)

```bash
#!/usr/bin/env bash

# Function for automatic touch device detection
detect_touch_device() {
    echo "Searching for touch devices..." >&2

    # Search for devices by patterns, excluding stylus
    local patterns=(
        "/dev/input/by-id/*Touchscreen*event*"
        "/dev/input/by-id/*touch*event*"
    )

    for pattern in "${patterns[@]}"; do
        for device in $pattern; do
            # Exclude stylus devices by name
            if [[ "$device" != *"mouse"* ]] && \
               [[ "$device" != *"stylus"* ]] && \
               [[ "$device" != *"pen"* ]] && \
               [ -e "$device" ] && [ -r "$device" ]; then
                echo "Found device: $device" >&2
                echo "$device"
                return 0
            fi
        done
    done

    echo "Error: No touch devices found" >&2
    return 1
}

# Main execution
main() {
    local config_dir="${XDG_CONFIG_HOME:-$HOME/.config}/niri-lisgd"
    local device_file="$config_dir/device"

    # Create config directory
    mkdir -p "$config_dir"

    # Check if device file already exists
    if [ -f "$device_file" ]; then
        local existing_device=$(cat "$device_file")
        if [ -r "$existing_device" ]; then
            echo "Using existing device from cache: $existing_device" >&2
            echo "$existing_device"
            return 0
        else
            echo "Cached device not accessible, re-detecting..." >&2
            rm -f "$device_file"
        fi
    fi

    # Auto-detect device
    echo "Auto-detecting touch device..." >&2
    local device=$(detect_touch_device)

    if [ $? -ne 0 ] || [ -z "$device" ]; then
        echo "Error: Failed to auto-detect compatible touch device" >&2
        return 1
    fi

    # Save device to file
    echo "$device" > "$device_file"
    echo "Auto-detected and cached device: $device" >&2
    echo "$device"
}

main
```

## 2. Упрощенный скрипт запуска (`~/.local/bin/niri-lisgd`)

```bash
#!/usr/bin/env bash

# Configuration
CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/niri-lisgd"
DEVICE_FILE="$CONFIG_DIR/device"

# Check if device file exists
if [ ! -f "$DEVICE_FILE" ]; then
    echo "Error: Device not configured. Run niri-lisgd-device-setup first" >&2
    exit 1
fi

# Read device from file
NIRI_LISGD_DEVICE=$(cat "$DEVICE_FILE")

# Verify device exists and is readable
if [ ! -r "$NIRI_LISGD_DEVICE" ]; then
    echo "Error: Device $NIRI_LISGD_DEVICE is not accessible" >&2
    echo "Please run niri-lisgd-device-setup to reconfigure" >&2
    exit 1
fi

# Start lisgd with gestures
exec lisgd -d "$NIRI_LISGD_DEVICE" -t 10 -T 5 \
    -g "1,RL,R,*,R,niri msg action focus-column-right" \
    -g "1,LR,L,*,R,niri msg action focus-column-left" \
    -g "1,DU,B,*,R,niri msg action open-overview"
```

## 3. Обновленный systemd юнит (`~/.config/systemd/user/niri-lisgd.service`)

```ini
[Unit]
Description=Touch Screen Gesture Daemon
After=graphical-session.target
Wants=graphical-session.target

[Service]
Type=simple
ExecStart=%h/.local/bin/niri-lisgd
Restart=on-failure
RestartSec=3

[Install]
WantedBy=graphical-session.target
```

## 4. Сервис однократной настройки (опционально) (`~/.config/systemd/user/niri-lisgd-setup.service`)

```ini
[Unit]
Description=Niri LISGD Device Setup
Before=niri-lisgd.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=%h/.local/bin/niri-lisgd-device-setup

[Install]
WantedBy=default.target
```

## Установка и использование:

1. **Сделайте скрипты исполняемыми:**
   ```bash
   chmod +x ~/.local/bin/niri-lisgd-device-setup
   chmod +x ~/.local/bin/niri-lisgd
   ```

2. **Выполните настройку устройства один раз:**
   ```bash
   ~/.local/bin/niri-lisgd-device-setup
   ```

3. **Или включите сервис настройки:**
   ```bash
   systemctl --user enable niri-lisgd-setup.service
   systemctl --user start niri-lisgd-setup.service
   ```

4. **Включите основной сервис:**
   ```bash
   systemctl --user enable niri-lisgd.service
   systemctl --user start niri-lisgd.service
   ```

## Преимущества этого подхода:

- **Однократное определение устройства** при первом запуске
- **Кэширование результата** в файле конфигурации
- **Более простая отладка** - можно проверить файл устройства
- **Упрощенный основной сервис** - только запуск lisgd
- **Уникальное имя переменной** `NIRI_LISGD_DEVICE`
- **Автоматическое переопределение** при недоступности закэшированного устройства

При необходимости ручного указания устройства можно просто создать файл `~/.config/niri-lisgd/device` с нужным путем.

## Resources

### Official

- site:
- repo:
- docs:

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
- name: Apply niri-lisgd configuration to local node
  hosts: localhost
  roles:
    - role: arcde.kotami.niri_lisgd
```

```yaml
- name: Apply niri-lisgd configuration to local node
  hosts: localhost
  roles:
    - role: arcde.kotami.niri_lisgd
      tags:
        - laptop
        - desktop
```
