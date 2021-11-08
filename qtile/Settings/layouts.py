from libqtile import  layout
from libqtile.config import  Match

layout_conf = {
    'border_focus': '#3E4377',
    'margin': 5,
    'border_width': 2,

}


layouts = [
    layout.Max(),
    layout.Columns(**layout_conf),
    
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_conf),
    layout.Bsp(**layout_conf),
    # layout.Matrix(**layout_conf),
    layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]




floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'), # gitk
        Match(wm_class='makebranch'), # gitk
        Match(wm_class='maketag'), # gitk
        Match(wm_class="pavucontrol"),  
        Match(wm_class="scrcpy"),  
        Match(wm_type="notification"),
        # Match(wm_class="download"),
        # Match(wm_class="thunar"),  
        # Match(wm_class="Thunderbird"),

        # Match(wm_class="transmission"),
        # Match(wm_class="gnome-calendar"),
        
        Match(wm_class='ssh-askpass'), # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'), # GPG key password entry
    ], border_focus = '#F05945'
)