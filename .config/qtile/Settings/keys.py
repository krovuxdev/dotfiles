
from os import path

from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.utils import guess_terminal
from Settings.path import qtile_path

# from Xlib import X
# from Xlib.display import Display


terminal = guess_terminal()
mod = "mod4"
mod1 = "mod1"
keys = [
    # hide/show bar
    Key([mod], "F1", lazy.hide_show_bar("all"), desc="Debugging hotkey",),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),

    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    # mondtall
    Key([mod], "space", lazy.layout.next(), lazy.layout.rotate(),
        desc="Move window focus to other window"),
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Move window focus to other window"),


    # Tile
    Key([mod, "shift"], "i", lazy.layout.increase_ratio()),
    Key([mod, "shift"], "o", lazy.layout.decrease_ratio()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating on focused window",
    ),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key(
        [mod],
        "F11",
        lazy.window.toggle_fullscreen(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    # open in terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Somethimes it breaks :(
    Key([mod], "u", lazy.spawn("emojimart")), ## Required install emojimart
    # Capture screen(flameshot)
    Key([mod, "shift", ], "s", lazy.spawn("flameshot gui")),


    # Browser internet
    Key([mod], "b", lazy.spawn("firefox")),
    # explorer
    Key([mod], "e", lazy.spawn("thunar")),



    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),


    #compton 
    Key([mod], "v", lazy.spawn([path.join(qtile_path, 'compton.sh')])),

    # Menu rofi
    # launcher
    Key([mod], "m", lazy.spawn([path.join(qtile_path, 'launcher.sh'), 'drun'])),
    Key([mod, "shift"], "m", lazy.spawn([path.join(qtile_path, 'launcher.sh'), 'window'])),
    Key([mod, "control"], "m", lazy.spawn([path.join(qtile_path, 'launcher.sh'), 'run'])),

    # Key([mod], "m", lazy.spawn("rofi -show drun")),
    # Key([mod, "control"], "m", lazy.spawn("rofi -show run")),
    # Window Nav rofi
    # Key([mod, "shift"], "m", lazy.spawn("rofi -show")),



    # PLay/pausa
    # Requirement install playerctl
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "Pause", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),

    Key([], "Scroll_Lock", lazy.spawn("xset led on "),
        lazy.spawn("setleds -D +num &")),
    Key([mod], "Scroll_Lock", lazy.spawn("xset led off")),

    # Key([mod], "i", lazy.spawn(terminal, "-e htop")), ##obsolete

    # Cambio monitor focus
    Key([mod], "p", lazy.to_screen(1)),
    Key([mod], "o", lazy.to_screen(0)),
    Key([mod1], "space", lazy.next_screen()),

    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        # "pamixer -i 5 --allow-boost changevolume down"
        "changevolume up"
    )),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn(
        "changevolume up-100"
    )),
    Key([mod, "control"], "XF86AudioRaiseVolume", lazy.spawn(
        # "pamixer -i 5 --allow-boost changevolume down"
        "changevolume up-ilimited"
    )),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        # "pamixer -d 5 --allow-boost"
        "changevolume down"
    )),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn(
        "changevolume down-0"
    )),
    Key([mod, "control"], "XF86AudioLowerVolume", lazy.spawn(
        # "pamixer -d 5 --allow-boost"
        "changevolume down-ilimited"
    )),





    # muted

    # caundo tenga el boton de teclado sea muted
    # muteado 
    # Key([], "XF86AudioMute", lazy.spawn(
    #     "pamixer -m"
    # )),

    




]
# d= Display()

# keysym_map ={
#     X.K_Alt_R:X.K_Alt_L,
# }

# for k,new_k in keysym_map:
#     k =d.keysym_to_string(k)
#     new_k = d.keysym_to_string(new_k)
#     keys.keylist.append([mod],k,lazy.spawn(f"xmodmap -e 'keycode' 108 = {new_k}"))
