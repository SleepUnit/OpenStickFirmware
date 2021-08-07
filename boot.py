import board
import usb_hid
from direct_input import DirectInput

# Add Appropriate HID Descriptor.
direct_input = DirectInput()
devices = [direct_input.device()]
usb_hid.enable(devices)