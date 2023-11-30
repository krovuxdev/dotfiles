from libqtile import hook

from typing import List  # noqa: F401

from os import path
import subprocess


from Settings.screens import screens
from Settings.widgets import widget_defaults, extension_defaults
from Settings.keys import mod, keys
from Settings.mouse import mouse
from Settings.groups import groups
from Settings.layouts import layouts, floating_layout
from Settings.path import qtile_path


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostarts.sh')])

main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


auto_fullscreen = True
focus_on_window_activation = "urgent" #smart urgent 
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"










