from logging import fatal
from typing import Text
from libqtile import widget, qtile
from libqtile.widget import net, cpu, memory, clock, windowname, textbox,  sep, canto
# from .themes import colors
from themes import Colors

def frec(bg,fg):
    return widget.CPU(
        font='UbuntuMono Nerd Font',
        foreground = fg,
        background = bg,
        format = 'CPU {freq_current}GHz {load_percent}%',
    ),


#Para mostrar Wifi y color
def Net(bg, fg):
    return widget.Net(
        interface = 'enp1s0f0u3',
        font='UbuntuMono Nerd Font',
        foreground = fg,
        background = bg,
        format = '直 {down} ↓↑ {up}',
        fontsize = 15,
    ),


def Memory(bg,fg):
    return widget.Memory(
        font='UbuntuMono Nerd Font',
        color=["#fffff"],
        foreground = fg,
        background = bg,
        format = '{MemUsed: .0f}{mm} //{MemTotal: .0f}{mm} ',
        measure_mem = "M",
        measure_swap = "M",
    ),



def LayoutCurrent(bg,fg):
    return widget.CurrentLayout(
        background = bg,
        foreground = fg,
    ),
def LayoutCurrentIcon(bg):
    return widget.CurrentLayoutIcon(
        background = bg,
        scale = 0.65
    ),

def Clock(bg,fg):
    return widget.Clock(
        format='  %Y/%m/%d %a   %I:%M:%S %p ',
        background = bg,
        foreground = fg,
    ),

def workspaces():
    return [
        widget.GroupBox(
            foreground=["#8AE49F", "#8AE49F"],
            background=["#141829", "#141829"],
            font='UbuntuMono Nerd Font',
            # margin_y=4,
            margin_x=0,
            # padding_y=4,
            padding_x=3,
            borderwidth=2,
            center_aligned = True,
            fontsize=18,
            active=["#ffffff", "#ffffff"], #active light
            inactive=["#4D727E", "#4D727E"],
            rounded=False,
            highlight_method='block',
            this_current_screen_border=["#F05945","#F05945"], #Focus_border_screen para icon color fondo selecionado barra
            # this_screen_border=["#F15C5C", "#4C4C4C"], #Gris
            other_current_screen_border=["#F05945","#F05945"], #Focus_border_screen_dark icon donde  esat cogiendo ventana
            # other_screen_border=["#141829", "#87DFD6"],
        ),
        widget.WindowName(
            foreground=["#EBF5EE", "#EBF5EE"],
            background=["#141829", "#141829"],
            fontsize=12,
            font='UbuntuMono Nerd Font bold',
            format = '{state}',
            # {name}
        ),

        # widget.Prompt(),
        # widget.TextBox("default config", name="default"),
        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

    ]


# ["#5F1854","#5F1854"]
def paletasBox(bg,fg):
    return widget.TextBox(
        background = bg,
        foreground = fg,
        text =  '',
        fontsize = 37,
        padding = -2,
    ),
def chord():
    return widget.Chord(
        chords_colors={
            'launch': ("#141829", "#141829"),
        },
        name_transform=lambda name: name.upper(),
    ),

def open_menu():
    qtile.cmd_spawn(".config/qtile/PowerOff.sh") 


def poweroff(bg,fg):
    return widget.TextBox(
        foreground = fg,
        background = bg,
        mouse_callbacks = {"Button1": open_menu},
        text =  '拉 ',
        fontsize=20,
    ),

def Systray(bg):
    return widget.Systray(
        background = bg,
    ),


primary_widgets = [

    #Base_layout_icon
    *workspaces(),
    *chord(),
    #For_icons
    *Systray(Colors.colorBG['bluedark']),
    #frecuency memory
    *paletasBox(Colors.colorBG['bluedark'],Colors.colorFG['orange']),
    *Memory(Colors.colorBG['orange'],Colors.colorFG['white']),
    #frecuencia cpu
    *paletasBox(Colors.colorBG['orange'],Colors.colorFG['redacuarela']),
    *frec(Colors.colorBG['redacuarela'],Colors.colorFG['white']),
    *paletasBox(Colors.colorBG['redacuarela'],Colors.colorFG['blueacuarela']),
    #Show Wifi
    *Net(Colors.colorBG['blueacuarela'], Colors.colorFG['white']),
    #midleewall
    *paletasBox(Colors.colorBG['blueacuarela'],Colors.colorFG['purple']),
    *LayoutCurrentIcon(Colors.colorBG['purple']),
    *LayoutCurrent(Colors.colorBG['purple'],Colors.colorFG['white']),
    *paletasBox(Colors.colorBG['purple'],Colors.colorFG['blueacuareladark']),
    #Hours
    *Clock(Colors.colorBG['blueacuareladark'],  Colors.colorFG['white']),
    *paletasBox(Colors.colorFG['blueacuareladark'],Colors.colorFG['orange']),
    *poweroff(Colors.colorBG['orange'], Colors.colorFG['white']),

]

secondary_widgets = [
    
    #Base_layout_icon
    *workspaces(),
    *chord(),
    #For_icons
    # *Systray(),
    # *paletasBox(),
    #frecuency memory
    *paletasBox(Colors.colorBG['bluedark'],Colors.colorFG['orange']),
    *Memory(Colors.colorBG['orange'],Colors.colorFG['white']),
    #frecuencia cpu
    *paletasBox(Colors.colorBG['orange'],Colors.colorFG['redacuarela']),
    *frec(Colors.colorBG['redacuarela'],Colors.colorFG['white']),
    *paletasBox(Colors.colorBG['redacuarela'],Colors.colorFG['blueacuarela']),
    #Show Wifi
    *Net(Colors.colorBG['blueacuarela'], Colors.colorFG['white']),
    #midleewall
    *paletasBox(Colors.colorBG['blueacuarela'],Colors.colorFG['purple']),
    *LayoutCurrentIcon(Colors.colorBG['purple']),
    *LayoutCurrent(Colors.colorBG['purple'],Colors.colorFG['white']),
    # *Separator(),
    *paletasBox(Colors.colorBG['purple'],Colors.colorFG['blueacuareladark']),
    #Hours
    *Clock(Colors.colorBG['blueacuareladark'],  Colors.colorFG['white']),
    *paletasBox(Colors.colorBG['blueacuareladark'],Colors.colorFG['orange']),
    *poweroff(Colors.colorBG['orange'], Colors.colorFG['white']),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font',
    'fontsize': 15,
    'padding': 6,
}
extension_defaults = widget_defaults.copy()





