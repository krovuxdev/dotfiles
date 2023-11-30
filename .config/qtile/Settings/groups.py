from libqtile.config import Group, Key
from libqtile.config import Match

from libqtile.lazy import lazy

from .keys import mod, keys


# groups = [Group(i, label='  ') for i in lista]


# \ue0b4 right
# \uE0B6 left

#  ["#f8e4d7", "#f8e4d7", "#f8e4d7"],

#  Group("c", matches=[Match(wm_class=["Firefox"])])

###########################################################################

# groups = [Group(i) for i in [" ",  "",  " ", " ", " ", " "]]
groups = [Group(i) for i in ["つ",  "二",  "三", "ッ", "五", "六"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], actual_key,  lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "Shift"], actual_key, lazy.window.togroup(group)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

###########################################################################


# @lazy.function
# def window_to_prev_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i - 1].name)


# @lazy.function
# def window_to_next_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i + 1].name)


# groups = [
#     Group("1", label=" "),
#     Group("2", label=" "),
#     Group("3", label=" "),
#     # Group(""),
#     # Group(" "),
#     # Group(" "),
#     # Group(" "),
#     # Group(" "),
# ]

# for i in enumerate(groups):
#     keys.extend([
#         Key([mod], i.groups, lazy.groups[i.group].toscreen())
#     ])
