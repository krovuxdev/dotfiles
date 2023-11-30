from libqtile import widget, qtile
from libqtile.widget import net, cpu, memory, clock, windowname, textbox,  sep, canto, groupbox, currentlayout, volume, textbox, wallpaper
from libqtile import bar
from themes import Colors

def Hd():
    return widget.Wallpaper(
        directory='~/.config/Wallpaper/',
        background='#15181a',
        foreground='#90b1c9',
        label='󰸉 HD',
        wallpaper='Wallpaper',
        fmt='󰸉 HD'
    ),
def spacer(bg):
    return widget.Spacer(
        bar.STRETCH,
        background=bg,
    ),
def frec(bg, fg):
    return widget.CPU(
        # font='UbuntuMono Nerd Font',
        foreground=fg,
        background=bg,
        format='CPU/GHz {freq_current}/{load_percent}%',
    ),

# Show Wifi and internet
def Net(bg, fg):
    return widget.Net(
        interface='enp1s0f0u3',
        # font='UbuntuMono Nerd Font',
        foreground=fg,
        background=bg,
        format='󱚽 {down} ↓↑ {up}',
        # fontsize=15,
    ),


def Memory(bg, fg):
    return widget.Memory(
        # font='UbuntuMono Nerd Font',
        color=["#fffff"],
        foreground=fg,
        background=bg,
        format='{MemUsed: .0f}{mm} //{MemTotal: .0f}{mm}',
        measure_mem="M",
        measure_swap="M",
        # fontsize=18
    ),


def LayoutCurrent(bg, fg):
    return widget.CurrentLayout(
        background=bg,
        foreground=fg,
    ),


def LayoutCurrentIcon(bg):
    return widget.CurrentLayoutIcon(
        background=bg,
        scale=0.65
    ),


def Clock(bg, fg):
    return widget.Clock(
        format='  %y/%m/%d %a   %I:%M:%S',
        background=bg,
        foreground=fg,
    ),

# \ue0b4 right
# \uE0B6 left
def workspaces():
    return widget.GroupBox(
        # foreground="#8AE49F",
        background="#15181a",
        borderwidth=1,
        active="#d4d4d4",  # active light
        inactive="#90b1c9",
        padding=3,
        spacing=5,
        disable_drag= True,
        hide_unused=False,
        center_aligned=True,
        rounded=True,
        highlight_method='line',
        highlight_color = "#15181a",
        this_current_screen_border="#fa314a",
        urgent_alert_method="text",
        # border= "#fa314a",
        # max_chars=0,
        # padding_y=2,
        # padding_x=2,
        # fontsize=14,
        # font='UbuntuMono Nerd Font',
        # margin_y=2,
        # margin_x=1,
        # Focus_border_screen para icon color fondo selecionado barra
        # this_screen_border="#4C4C4C",  # Gris
        # Focus_border_screen_dark icon donde  esat cogiendo ventana
    ),
    


def Nametxt():
    return widget.WindowName(
        foreground=["#EBF5EE", "#EBF5EE"],
        background="#000000",
        # fontsize=10,
        padding=0,
        # font='UbuntuMono Nerd Font bold',
        format='{state}{name}',
    ),
# ["#5F1854","#5F1854"]


def paletasBox(bg, fg, lb = '', fs = 18):
    return widget.TextBox(
        background=bg,
        foreground=fg,
        text=lb,
        fontsize=fs,
        # padding=15,
    ),


def wgbox():
    return widget.WidgetBox(widgets=[
        *Memory(Colors.colorBG['orange'], Colors.colorFG['white']),
        *Systray(Colors.colorBG['bluedark'], Colors.colorBG['orange']),


    ],
        close_button_location='right',
        text_closed=' < ',
        text_open=' > ',

    ),


def paletasBox2(bg, fg):
    return widget.TextBox(
        background=bg,
        foreground=fg,
        # text =  '',
        fontsize=7,
        padding=1,
    ),


def wtb(bg, fg):
    return widget.WindowTabs(
        background=bg,
        foreground=fg,
        # text =  '',
        # fontsize=37,
    ),


def chord():
    return widget.Chord(
        chords_colors={
            'launch': ("#141829", "#141829"),
        },
        name_transform=lambda name: name.upper(),
    ),


def open_menu():
    qtile.cmd_spawn(".config/qtile/script/PowerOff.sh")


def poweroff(bg, fg):
    return widget.TextBox(
        foreground=fg,
        background=bg,
        mouse_callbacks={"Button1": open_menu},
        text='󰣇',
        fontsize=18,
    ),


def Systray(bg, fg):
    return widget.Systray(
        background=bg,
        foreground=fg,
        icon_size=15
        # padding=5
    ),

def pvolumen(bg, fg):
    return widget.PulseVolume(
        background=bg,
        foreground=fg,
        font="MesloLGS NF",
        # fontsize=16,
        limit_max_volume=False,
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        update_interval=0.01,
    ),
def separator(bg):
    return widget.Sep(
        linewidth=0, 
        padding=5,
        background=bg,
        ),

primary_widgets = [
    # Base_layout_icon
    *workspaces(),
    # *paletasBox("#00000000", Colors.colorFG['bluedark'], '',30),
    *spacer(Colors.colorBG['accuarela']),
    # *Nametxt(),
    # *wtb(Colors.colorBG['bluedark'], Colors.colorBG['orange']),
    # *wgbox(),
    # *chord(),
    # For_icons
    *Hd(),
    # *separator(Colors.colorBG['Dark']),
    # frecuency memory
    # *paletasBox(Colors.colorBG['bluedark'], Colors.colorFG['orange']),
    *Memory(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # *separator(Colors.colorBG['Dark']),
    # frecuencia cpu
    *paletasBox(Colors.colorBG['Dark'], Colors.colorFG['accuarela'],lb='󰍛'),
    *frec(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # *paletasBox(Colors.colorBG['redacuarela'], Colors.colorFG['blueacuarela']),
    # Show Wifi
    # *separator(Colors.colorBG['Dark']),
    *Net(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # midleewall
    # *separator(Colors.colorBG['Dark']),
    # *paletasBox(Colors.colorBG['blueacuarela'], Colors.colorFG['purple']),
    # *LayoutCurrentIcon(Colors.colorBG['Dark']),
    # *LayoutCurrent(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # *separator(Colors.colorBG['Dark']),
    # *paletasBox(Colors.colorBG['purple'], Colors.colorFG['blueacuareladark']),
    # Hours
    # *separator(Colors.colorBG['Dark']),
    *Clock(Colors.colorBG['Dark'],  Colors.colorFG['accuarela']),
    # *separator(Colors.colorBG['Dark']),
    # *paletasBox(Colors.colorFG['blueacuareladark'], Colors.colorFG['orange']),
    *poweroff(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    *Systray(Colors.colorBG['Dark'], Colors.colorBG['accuarela']),

    *separator(Colors.colorBG['Dark']),
]

secondary_widgets = [
    # Base_layout_icon
    *workspaces(),
    # *paletasBox("#00000000", Colors.colorFG['bluedark'], '',30),
    *spacer(Colors.colorBG['Dark']),
    # *Nametxt(),
    # *wtb(Colors.colorBG['bluedark'], Colors.colorBG['orange']),
    # *wgbox(),
    # *chord(),
    # For_icons
    # *Systray(Colors.colorBG['Dark'], Colors.colorBG['orange']),
    # *separator(Colors.colorBG['Dark']),
    # frecuency memory
    # *paletasBox(Colors.colorBG['bluedark'], Colors.colorFG['orange']),
    *Memory(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # *separator(Colors.colorBG['Dark']),
    # frecuencia cpu
    # *paletasBox(Colors.colorBG['orange'], Colors.colorFG['redacuarela']),
    *frec(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # *paletasBox(Colors.colorBG['redacuarela'], Colors.colorFG['blueacuarela']),
    # Show Wifi
    # *separator(Colors.colorBG['Dark']),
    *Net(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # midleewall
    # *separator(Colors.colorBG['Dark']),
    # *paletasBox(Colors.colorBG['blueacuarela'], Colors.colorFG['purple']),
    # *LayoutCurrentIcon(Colors.colorBG['Dark']),
    # *LayoutCurrent(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),
    # *separator(Colors.colorBG['Dark']),
    # *paletasBox(Colors.colorBG['purple'], Colors.colorFG['blueacuareladark']),
    # Hours
    # *separator(Colors.colorBG['Dark']),
    *Clock(Colors.colorBG['Dark'],  Colors.colorFG['accuarela']),
    # *separator(Colors.colorBG['Dark']),
    # *paletasBox(Colors.colorFG['blueacuareladark'], Colors.colorFG['orange']),
    *poweroff(Colors.colorBG['Dark'], Colors.colorFG['accuarela']),

    # *separator(Colors.colorBG['Dark']),

]

three_widgets = [
    # *pvolumen(Colors.colorBG['orange'], Colors.colorFG['white']),
    # Base_layout_icon
    # *Nametxt(),
    *paletasBox2(Colors.colorBG['bluedark'], Colors.colorFG['orange']),
    *chord(),
    # For_icons
    # *Systray(),
    # *paletasBox(),
    # frecuency memory
    *paletasBox(Colors.colorBG['bluedark'], Colors.colorFG['orange']),
    *Memory(Colors.colorBG['orange'], Colors.colorFG['white']),
    # frecuencia cpu
    *paletasBox(Colors.colorBG['orange'], Colors.colorFG['redacuarela']),
    *frec(Colors.colorBG['redacuarela'], Colors.colorFG['white']),
    *paletasBox(Colors.colorBG['redacuarela'], Colors.colorFG['blueacuarela']),
    # Show Wifi
    *Net(Colors.colorBG['blueacuarela'], Colors.colorFG['white']),
    # midleewall
    *paletasBox(Colors.colorBG['blueacuarela'], Colors.colorFG['purple']),
    *LayoutCurrentIcon(Colors.colorBG['purple']),
    *LayoutCurrent(Colors.colorBG['purple'], Colors.colorFG['white']),
    # *Separator(),
    *paletasBox(Colors.colorBG['purple'], Colors.colorFG['blueacuareladark']),
    # Hours

    *Clock(Colors.colorBG['blueacuareladark'],  Colors.colorFG['white']),
    *paletasBox(Colors.colorBG['blueacuareladark'], Colors.colorFG['orange']),
    *poweroff(Colors.colorBG['orange'], Colors.colorFG['white']),

]

widget_defaults = {
    # 'font': 'UbuntuMono Nerd Font',
    'font': 'HackNerdFont',
    'fontsize': 11,
    'padding': 5,
}
extension_defaults = widget_defaults.copy()
