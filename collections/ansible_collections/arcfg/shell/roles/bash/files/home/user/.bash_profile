# ~/.bash_profile: executed by the command interpreter for login shells.
# This is a bootstrap file that sources the main configuration from XDG location.

# Source the main bash_profile from XDG config directory
if [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/bash/.bash_profile" ]; then
    . "${XDG_CONFIG_HOME:-$HOME/.config}/bash/.bash_profile"
fi
