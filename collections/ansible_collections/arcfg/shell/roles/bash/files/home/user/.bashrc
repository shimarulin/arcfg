# ~/.bashrc: executed by bash(1) for non-login shells.
# This is a bootstrap file that sources the main configuration from XDG location.

# Source the main bashrc from XDG config directory
if [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/bash/.bashrc" ]; then
    . "${XDG_CONFIG_HOME:-$HOME/.config}/bash/.bashrc"
fi
