# ~/.config/bash/.bash_profile: executed by the command interpreter for login shells.
# Main bash profile configuration using XDG Base Directory Specification.

# Source .profile if it exists
if [ -f "$HOME/.profile" ]; then
    . "$HOME/.profile"
fi

# Source .bashrc if it exists (for interactive shells)
if [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/bash/.bashrc" ]; then
    . "${XDG_CONFIG_HOME:-$HOME/.config}/bash/.bashrc"
fi
