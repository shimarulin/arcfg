#!/usr/bin/env bash

# for i in {0..7}; do print -Pn "%K{$i}  %k%F{$i}${(l:3::0:)i}%f " ${${(M)$((i%6)):#3}:+$'\n'}; done

# Define color codes
declare -A colors
colors[black]="\033[0;30m"
colors[red]="\033[0;31m"
colors[green]="\033[0;32m"
colors[yellow]="\033[0;33m"
colors[blue]="\033[0;34m"
colors[magenta]="\033[0;35m"
colors[cyan]="\033[0;36m"
colors[white]="\033[0;37m"

# Define bright color codes
declare -A bright_colors
bright_colors[black]="\033[0;90m"
bright_colors[red]="\033[0;91m"
bright_colors[green]="\033[0;92m"
bright_colors[yellow]="\033[0;93m"
bright_colors[blue]="\033[0;94m"
bright_colors[magenta]="\033[0;95m"
bright_colors[cyan]="\033[0;96m"
bright_colors[white]="\033[0;97m"

# Print color palette
echo "Normal Colors:"
for color in "${!colors[@]}"; do
  echo -e "${colors[$color]}$color"
done

echo -e "\nBright Colors:"
for color in "${!bright_colors[@]}"; do
  echo -e "${bright_colors[$color]}$color"
done

# Reset color
echo -e "\033[0m"
