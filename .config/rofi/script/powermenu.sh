#!/usr/bin/bash

# dir="$HOME/.config/rofi/configs/"
dir="$HOME/.config/rofi/styles/"
# rofi_command="rofi -theme $dir/dark.rasi"
rofi_command="rofi -theme $dir/powerdark.rasi"
rofi_command2="rofi -theme $dir/confirm.rasi"

iconspower="⏻"
iconsreboot="⏼"
iconsupends="⭘"
iconslock=""
iconslogout="﫼"
# Options
shutdown="$iconspower shutdown"
reboot="$iconsreboot reboot"
suspend="$iconsupends suspend"
lock="$iconslock lock"
logout="$iconslogout logout"

# confirm_exit() {
# 	rofi -dmenu\
# 		-i\
# 		-no-fixed-num-lines\
# 		-p "Esta seguro? Y/N : "\
# 		-theme $HOME/.config/rofi/styles/confirm.rasi
# }
# uptime=$(uptime -p | sed -e 's/up //g')
confirm_exit(){
	if ! [[ $(echo -e "Yes\nNo" | $rofi_command2 -p "Esta seguro?" -dmenu -select-row 2) == Yes ]]; then
		exit 0
	fi
}

# options="$shutdown\n$reboot\n$suspend\n$lock"
options="$shutdown\n$reboot\n$lock\n$logout"
chosen="$(echo -e "$options" | $rofi_command -p "Search" -dmenu -selected-row 2)"

case $chosen in
    $shutdown)
			confirm_exit
			poweroff
		;;
    $reboot)
			confirm_exit
			reboot
		;;
    $lock)
			confirm_exit
			i3lock
		;;
	$logout)
		confirm_exit
		killall -u $USER
	;;
esac

