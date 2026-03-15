# ~/.profile: executed by the command interpreter for login shells.
# This file is sourced by all shells (bash, zsh, etc.) on login.

# Load profiles from $XDG_CONFIG_HOME/profile.d
profiles_path="${XDG_CONFIG_HOME:-$HOME/.config}/profile.d"
if [ -d "$profiles_path" ]; then
  for profile in "$profiles_path"/*.sh; do
    [ -r "$profile" ] && . "$profile"
  done
  unset profile
fi
unset profiles_path
