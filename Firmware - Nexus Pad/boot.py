# type: ignore

# boot.py
# This runs before code.py in CircuitPython.
# KMK uses this to configure USB correctly for keyboard firmware.

import usb_cdc
import usb_hid

# Disable the serial console over USB (saves memory, avoids conflicts)
usb_cdc.disable()

# Enable USB HID (keyboard/mouse support)
usb_hid.enable()
