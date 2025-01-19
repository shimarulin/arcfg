# scheme: "tokyonight"
# source: "https://github.com/folke/tokyonight.nvim/blob/main/extras/tilix/tokyonight_night.json"
if [ "$TERM" = "linux" ]; then
    echo -en "\e]P01a1b26" #black    -> this is the background color as well.
    echo -en "\e]P1f7768e" #darkred
    echo -en "\e]P29ece6a" #darkgreen
    echo -en "\e]P3e0af68" #brown
    echo -en "\e]P47aa2f7" #darkblue
    echo -en "\e]P5bb9af7" #darkmagenta
    echo -en "\e]P67dcfff" #darkcyan
    echo -en "\e]P7a9b1d6" #lightgray
    echo -en "\e]P8414868" #darkgray
    echo -en "\e]P9f7768e" #red
    echo -en "\e]PA9ece6a" #green
    echo -en "\e]PBe0af68" #yellow
    echo -en "\e]PC7aa2f7" #blue
    echo -en "\e]PDbb9af7" #magenta
    echo -en "\e]PE7dcfff" #cyan
    echo -en "\e]PFc0caf5" #white    -> this is the foreground color as well.
    clear                  #repaint the whole background with the new color
fi
