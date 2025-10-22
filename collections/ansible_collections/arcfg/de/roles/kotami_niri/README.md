# Ansible Role "kotami_niri"

> Ansible role 'kotami-niri'

## Tablet mode support

https://yalter.github.io/niri/Configuration%3A-Switch-Events.html

```
switch-events {
    lid-close { spawn "notify-send" "The laptop lid is closed!"; }
    lid-open { spawn "notify-send" "The laptop lid is open!"; }
    tablet-mode-on { spawn "bash" "-c" "gsettings set org.gnome.desktop.a11y.applications screen-keyboard-enabled true"; }
    tablet-mode-off { spawn "bash" "-c" "gsettings set org.gnome.desktop.a11y.applications screen-keyboard-enabled false"; }
}
```

> Linux can detect tablet mode using the iio-sensor-proxy, which monitors the device's sensors to determine its
> orientation and whether it is in tablet mode. If the sensors are functioning correctly, the system should
> automatically disable the keyboard and touchpad while enabling touch features when the device is flipped into tablet
> mode.

1. Use 'detect tablet mode' script to enable/disable tablet features

- https://github.com/alesya-h/linux_detect_tablet_mode/blob/master/watch_tablet
- https://bbs.archlinux.org/viewtopic.php?id=288645
- https://askubuntu.com/questions/1540423/tablet-mode-event-detection-on-hp-spectre-x360

2. If tablet mode detected, run https://github.com/Zhaith-Izaliel/iio-niri to autorotate monitor (and stop if laptop
   mode)

## On-screen keyboard

To automatically show the on-screen keyboard in Niri when switching to tablet mode, you can set up a Udev rule to detect
the tablet mode switch and launch the keyboard. Additionally, enabling the on-screen keyboard from your system's
accessibility settings may help.

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
- name: Apply kotami-niri configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.de.kotami_niri
```

```yaml
- name: Apply kotami-niri configuration to local node
  hosts: localhost
  roles:
    - role: arcfg.de.kotami_niri
      tags:
        - laptop
        - desktop
```
