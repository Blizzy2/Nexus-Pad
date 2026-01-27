"""
Nexus pad (Xiao RP2040 DIP) - KMK Firmware
========================================
What this file does?
-------------------
This file translates clicks on your MacroPad to opening/launching apps using AutoHotkey V2
------------------------------
Features of MY MacroPad:
- 6 Physical Buttons
- Layering System (Main + FN Layer)
- App-Launch Hotkeys for Windows
- Media + Utility Keys on the FN Layer
- Easy to adapt later (RGB + More Layers/More Macros)
"""

# ----------------------------
# 1)Imports (CircuitPython + KMK)
# ----------------------------

import board  # type: ignore

from kmk.kmk_keyboard import KMKKeyboard

from kmk.scanners.keypad import KeysScanner

from kmk.keys import KC

from kmk.layers import Layers # type: ignore

from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap

# ----------------------------
# 2)Keyboard Setup
# ----------------------------

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

macros = Macros()
keyboard.modules.append(macros)


# ----------------------------
# 3) Hardware wiring: define which GPIO pins are connected to the buttons 
#-----------------------------

PINS = [
    board.GP6,
    board.GP0,
    board.GP3,
    board.GP4,
    board.GP2,
    board.GP1,
]  

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ----------------------------
# 4) Launcher Hotkeys for Windows
# ----------------------------

LAUNCH_DISCORD_MEDAL = KC.LCTL(KC.LALT(KC.N1))  # Ctrl + Alt + 1
LAUNCH_NEXUS_AI = KC.LCTL(KC.LALT(KC.N2))  # Ctrl + Alt + 2
LAUNCH_STEAM = KC.LCTL(KC.LALT(KC.N3))  # Ctrl + Alt + 3
LAUNCH_VSCODE = KC.LCTL(KC.LALT(KC.N4)) # Ctrl + Alt + 4

# ----------------------------
# 5) Define Layers (Main + FN Layer)
# ----------------------------

"""
I will use 2 layers:
Layer 0: (Main Layer/Daily Use)
1) Discord + Medal
2) Nexus AI
3) Steam
4) VSCode
5) Mute/Unmute
6) FN (Hold) -> Switch to Layer 1
Layer 1: (FN / Utility)
1) Volume Up
2) Volume Down
3) Screenshot
4) Transparent
5) Next Track
6) Previous Track

This layout prioritizes tools I use daily when i turn on my PC.
"""

FN = KC.MO(1)  # Hold for Layer 1

SNIP_TOOL = KC.Macro(
    Press(KC.LGUI), Press(KC.LSFT), Tap(KC.S),
    Release(KC.LSFT), Release(KC.LGUI)
)

# ----------------------------
# 6) Keymaps (6 keys per layer)
# ----------------------------

keyboard.keymap = [
    # Layer 0: Main Layer
    [
        LAUNCH_DISCORD_MEDAL,  # Key 1: one-press "boot apps"
        LAUNCH_NEXUS_AI,       # Key 2: open Nexus AI (placeholder for now)
        LAUNCH_STEAM,          # Key 3: open Steam
        LAUNCH_VSCODE,         # Key 4: open VSCode
        KC.MUTE,               # Key 5: Mute/Unmute
        FN                     # Key 6: Hold for FN Layer
    ],
    # Layer 1: FN / Utility Layer
    [
        KC.VOLD,               # Key 1: Volume Down
        KC.VOLU,               # Key 2: Volume Up
        SNIP_TOOL,          # Key 3: Screenshot (Win + Shift + S)
        KC.TRNS,              # Key 4 (Transparent)
        KC.MNXT,              # Key 5: Next Track
        KC.MPRV               # Key 6: Previous Track
    ]
]

# ----------------------------
# 7) Placeholder for RGB (SK6812) - To be implemented later
# ----------------------------          
# from kmk.extensions.rgb import RGB
# rgb = RGB(pixel_pin=board.GP29, num_pixels=2)
# keyboard.extensions.append(rgb)

# ----------------------------
# 8) Start KMK
# ----------------------------

if __name__ == "__main__":
    keyboard.go()