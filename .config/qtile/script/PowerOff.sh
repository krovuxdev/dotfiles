#!/usr/bin/bash


dir="$HOME/.config/rofi"
script="script"
power="powermenu.sh"
if [[ -f "$HOME/.config/rofi/script/powermenu.sh" ]]; then
    ruta="$($dir/$script/$power)"
else
    rofi -show drun -theme .config/rofi/config.rasi
fi

