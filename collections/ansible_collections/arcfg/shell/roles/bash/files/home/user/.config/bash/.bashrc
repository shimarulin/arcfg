# ~/.config/bash/.bashrc: executed by bash(1) for non-login shells.
# Main bash configuration file using XDG Base Directory Specification.

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# Source sheldon plugins
eval "$(sheldon --config-dir ~/.config/sheldon/bash source)"

# Source .bashrc from profile.d if it exists (for interactive settings)
if [ -d "${XDG_CONFIG_HOME:-$HOME/.config}/profile.d" ]; then
    for profile in "${XDG_CONFIG_HOME:-$HOME/.config}/profile.d"/*.sh; do
        [ -r "$profile" ] && . "$profile"
    done
    unset profile
fi
