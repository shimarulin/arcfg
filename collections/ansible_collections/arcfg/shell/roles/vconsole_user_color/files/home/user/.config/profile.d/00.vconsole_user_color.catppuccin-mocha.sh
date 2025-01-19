# scheme: "Catppuccin Mocha"
# author: "https://github.com/catppuccin/catppuccin"
# source: "https://github.com/catppuccin/tilix/blob/main/themes/catppuccin-mocha.json"
# source: "https://github.com/catppuccin/st/blob/main/themes/mocha.h"
if [ "$TERM" = "linux" ]; then
    echo -en "\e]P01e1e2e" #black    -> this is the background color as well.
    echo -en "\e]P1f38ba8" #darkred
    echo -en "\e]P2a6e3a1" #darkgreen
    echo -en "\e]P3f9e2af" #brown
    echo -en "\e]P489b4fa" #darkblue
    echo -en "\e]P5f5c2e7" #darkmagenta
    echo -en "\e]P694e2d5" #darkcyan
    echo -en "\e]P7585b70" #lightgray
    echo -en "\e]P8a6adc8" #darkgray
    echo -en "\e]P9f38ba8" #red
    echo -en "\e]PAa6e3a1" #green
    echo -en "\e]PBf9e2af" #yellow
    echo -en "\e]PC89b4fa" #blue
    echo -en "\e]PDf5c2e7" #magenta
    echo -en "\e]PE94e2d5" #cyan
    echo -en "\e]PFcdd6f4" #white    -> this is the foreground color as well.
    clear                  #repaint the whole background with the new color
fi
