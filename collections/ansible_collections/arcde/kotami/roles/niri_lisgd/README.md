# Ansible Role "niri_lisgd"

> Run niri action by lisgd gestures

Для управления сервисом без sudo нужно создать пользовательский systemd сервис. Вот решение:

1. Создайте скрипт `~/.local/bin/lisgd-daemon`:

```bash
#!/bin/bash

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
    local device="$1"

    # Use manual device if provided, otherwise auto-detect
    if [ -n "$device" ]; then
        echo "Using manually specified device: $device" >&2
        DEVICE="$device"
    else
        echo "Auto-detecting touch device..." >&2
        DEVICE=$(detect_touch_device)
        if [ $? -ne 0 ] || [ -z "$DEVICE" ]; then
            echo "Error: Failed to auto-detect compatible touch device" >&2
            exit 1
        fi
        echo "Auto-detected compatible device: $DEVICE" >&2
    fi

    # Verify device exists and is readable
    if [ ! -r "$DEVICE" ]; then
        echo "Error: Device $DEVICE is not accessible" >&2
        exit 1
    fi

    # Start lisgd with gestures
    exec lisgd -d "$DEVICE" -t 10 -T 5 \
        -g "1,RL,R,*,R,niri msg action focus-column-right" \
        -g "1,LR,L,*,R,niri msg action focus-column-left" \
        -g "1,DU,B,*,R,niri msg action open-overview"
}

# Parse command line arguments
case "${1:-}" in
    -d|--device)
        main "$2"
        ;;
    "")
        main ""
        ;;
    *)
        echo "Usage: $0 [-d DEVICE_PATH]"
        echo "  -d, --device  Use specified device instead of auto-detection"
        exit 1
        ;;
esac
```

Сделайте скрипт исполняемым:
```bash
chmod +x ~/.local/bin/lisgd-daemon
```

2. Создайте директорию для пользовательских systemd сервисов, если её нет:
```bash
mkdir -p ~/.config/systemd/user
```

3. Создайте файл сервиса `~/.config/systemd/user/lisgd.service`:

```ini
[Unit]
Description=Touch Screen Gesture Daemon
After=graphical-session.target
Wants=graphical-session.target

[Service]
Type=simple
ExecStart=%h/.local/bin/lisgd-daemon
ExecStartPre=/bin/sleep 5
Restart=on-failure
RestartSec=3

# Optional: specify device manually by uncommenting and modifying next line
# Environment=DEVICE=/dev/input/eventX

[Install]
WantedBy=default.target
```

4. Активируйте и запустите сервис:

```bash
# Перезагрузить конфигурацию пользовательских сервисов
systemctl --user daemon-reload

# Включить автозапуск
systemctl --user enable lisgd.service

# Запустить сервис
systemctl --user start lisgd.service
```

5. Для автоматического запуска при входе в систему, включите lingering:

```bash
# Если используете systemd без полного логина в сессии
loginctl enable-linger $USER
```

Управление сервисом (без sudo):
```bash
# Статус
systemctl --user status lisgd

# Остановка
systemctl --user stop lisgd

# Запуск
systemctl --user start lisgd

# Перезагрузка
systemctl --user restart lisgd

# Просмотр логов
journalctl --user-unit=lisgd -f

# Включить автозапуск
systemctl --user enable lisgd

# Выключить автозапуск
systemctl --user disable lisgd
```

6. Для ручного указания устройства создайте конфигурационный файл:

```bash
mkdir -p ~/.config/systemd/user/lisgd.service.d/
```

Создайте `~/.config/systemd/user/lisgd.service.d/override.conf`:
```ini
[Service]
Environment=DEVICE=/dev/input/your_device_here
```

Или отредактируйте напрямую:
```bash
systemctl --user edit lisgd.service
```

Альтернативно, можно запускать с конкретным устройством через командную строку:
```bash
~/.local/bin/lisgd-daemon -d /dev/input/your_device
```

Преимущества этого подхода:
- Полностью пользовательский сервис, не требует root прав
- Автозапуск при входе пользователя
- Легкое управление через systemctl --user
- Возможность ручного указания устройства через переменные окружения или аргументы
- Интеграция с графической сессией

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
