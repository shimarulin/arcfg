#!/usr/bin/env zsh

# Set $STARSHIP_CONFIG if it empty or not defined
function {
  if [[ -z "$STARSHIP_CONFIG" ]]; then
    # Full colors and icons used by default
    local STARSHIP_CONFIG_NAME="jetpack"

    # Linux console fallback
    # Detect Linux console can be possible with "$TERM" = "linux" or `tput colors` = "8"
    if [ "$(tput colors)" = "8" ]; then
      STARSHIP_CONFIG_NAME="plain-text-symbols"
    fi

    export STARSHIP_CONFIG="${HOME}/.config/starship/${STARSHIP_CONFIG_NAME}.starship.toml"
  fi
}
