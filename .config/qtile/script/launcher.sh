#!/usr/bin/bash
dir="$HOME/.config/rofi"
script="script"
launcher="launcher.sh"
select=$1
function drun-rofi() {
    if [[ -f "$HOME/.config/rofi/script/launcher.sh" ]]; then
        ruta="$($dir/$script/$launcher)"
    else
        rofi -show drun -modi drun
    fi
}

function window-rofi(){
    rofi -show window -modi window -theme $HOME/.config/rofi/configs/menudark.rasi
}
function run-rofi(){
    rofi -show run -modi run -theme $HOME/.config/rofi/configs/menudark.rasi
}

if [[ $select == 'window' ]]; then
    window-rofi
elif [[ $select == 'drun' ]]; then
    drun-rofi
elif [[ $select == 'run' ]]; then
    run-rofi
fi