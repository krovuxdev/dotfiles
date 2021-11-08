from libqtile import  hook

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
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True

auto_minimize = True

# wmname = "LG3D"
wmname = "qtile"
