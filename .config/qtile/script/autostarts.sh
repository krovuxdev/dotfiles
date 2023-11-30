#!/bin/sh


# Wallpaper
# feh --bg-scale Imágenes/dom.jpg &

# Composer
compton --config $HOME/.config/qtile/conf/compton.conf &
# picom --experimental-backends &
function systrays(){
	# systray
	sleep 5 && volumeicon -d default &
	udiskie -t &
}


#controlador
# if  pgrep -f "pulseaudio"
# then
# 	pulseaudio &
# 	systrays
# else
# 	pkill pulseaudio &
# 	pulseaudio &
# 	systrays
# fi

# setxkbmap es &
# xset led on &
# setleds -D +num &
# bluetoothctl --monitor power on &
# sleep 4 && bluetoothctl --monitor connect 41:42:AA:01:1B:CB &







# Monitor
# xrandr --output DVI-I-0 --off --output DVI-I-1 --off --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-4 --off --output DP-5 --off &


