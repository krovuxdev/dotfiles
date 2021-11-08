userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset fs 
fi

# Screens
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

# if [ "$hdmi" = "HDMI-1" ]; then
#   xrandr --output eDP-1 --primary --mode 1366x768 --pos 276x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
# else
#   xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off &
# fi

# Keyboard Layout
setxkbmap es &

# Wallpaper
feh --bg-scale Imágenes/anime.jpg &
# Composer
picom &
xrandr --output DVI-I-0 --off --output DVI-I-1 --off --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-4 --off --output DP-5 --off &

xset led on &
setleds -D +num &
# volumeicon &

pulseaudio &
udiskie -t &
