from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets, secondary_widgets, three_widgets
from libqtile.log_utils import logger

import subprocess


def status_bar(widgets, ft=25, op=1.0, mg=[9, 5, 5, 5]):
    return bar.Bar(widgets, ft, opacity=op, margin=mg,background="#141829")


def src(slc, wgt=primary_widgets,hd="~/.config/Wallpaper/evangelio1.png"):
    if slc == 'top':
        return Screen(top=status_bar(wgt), left=bar.Gap(size=5), right=bar.Gap(size=5), bottom=bar.Gap(size=5),wallpaper=hd,wallpaper_mode='fill')
    if slc == 'bottom':
        return Screen(bottom=status_bar(wgt), left=bar.Gap(size=5), right=bar.Gap(size=5),wallpaper=hd,wallpaper_mode='fill')
    if slc == 'left':
        return Screen(left=status_bar(wgt), right=bar.Gap(size=5), bottom=bar.Gap(size=5),wallpaper=hd,wallpaper_mode='fill')
    if slc == 'right':
        return Screen(right=status_bar(wgt), left=bar.Gap(size=5), bottom=bar.Gap(size=5),wallpaper=hd,wallpaper_mode='fill')
    else:
        return Screen(bottom=status_bar(wgt),wallpaper=hd,wallpaper_mode='fill')


def src2(slc, wgt=primary_widgets, hd="~/.config/Wallpaper/evangelio1.png"):
    if slc == 'top':
        return Screen(top=status_bar(wgt),wallpaper=hd,wallpaper_mode='fill')
    if slc == 'bottom':
        return Screen(bottom=status_bar(wgt),wallpaper=hd,wallpaper_mode='fill')
    if slc == 'left':
        return Screen(left=status_bar(wgt),wallpaper=hd,wallpaper_mode='fill')
    if slc == 'right':
        return Screen(right=status_bar(wgt),wallpaper=hd,wallpaper_mode='fill')
    else:
        return Screen(bottom=status_bar(wgt),wallpaper=hd,wallpaper_mode='fill')


screens = [src2('top',hd='~/.config/Wallpaper/exquisito.png')]

# screens = [Screen(top=status_bar(primary_widgets), left=bar.Gap(
#     size=5), right=bar.Gap(size=5), bottom=bar.Gap(size=5))]


xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"


command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitor using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        # screens.append(Screen(top=status_bar(secondary_widgets)))
        screens.append(src2('top', wgt=secondary_widgets, hd="~/.config/Wallpaper/exquisito.png"))
