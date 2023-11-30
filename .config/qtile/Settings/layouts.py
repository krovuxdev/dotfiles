from libqtile import layout
from libqtile.config import Match

layout_conf = {
    'border_focus': '#11698E',
    'border_normal': '#141829',
    'border_width': 2,
    'margin': 5,
    'fair': True,

}


layouts = [
    layout.Max(),
    # layout.Columns(**layout_conf),

    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2, **layout_conf),
    layout.Bsp(**layout_conf),
    # layout.Matrix(**layout_conf),
    # layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.RatioTile(**layout_conf),
    layout.Tile(**layout_conf),
    # layout.TreeTab(**layout_conf),
    # layout.VerticalTile(**layout_conf),
    # layout.Zoomy(),
    layout.Floating(**layout_conf),
]


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="pavucontrol"),
        Match(wm_class="scrcpy"),
        # Match(wm_class="Blender_Preferences"),
        Match(wm_class="download"), 
        Match(wm_class="dialog"), 
        Match(wm_class="Emojimart"), 
        Match(wm_class="toolbar"), 
        Match(wm_class="error"),
        Match(wm_class="Ursina"),
        Match(wm_class="file_progress"),
        Match(wm_type="notification"),
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='confirm'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        # Match(wm_class="thunar"),
        # Match(wm_class="Thunderbird"),

        # Match(wm_class="transmission"),
        # Match(wm_class="gnome-calendar"),

    ], border_focus='#90b1c9', border_normal="#15181a"
)
