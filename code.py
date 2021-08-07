import board
import usb_hid
from ofs import OpenFightStick
from controls import Button, Directional
from leds import Leds
import neopixel

pixels = neopixel.NeoPixel(board.GP14, 16, brightness=0.3, auto_write=False)

buttons = [
    Button(board.GP0, 0, pixels, [4]), # 1P 
    Button(board.GP1, 3, pixels, [5]), # 2P
    Button(board.GP2, 5, pixels, [6]), # 3P
    Button(board.GP3, 4, pixels, [7]), # 4P
    Button(board.GP4, 1, pixels, [8]), # 1K
    Button(board.GP5, 2, pixels, [9]), # 2K
    Button(board.GP6, 7, pixels, [10]), # 3K
    Button(board.GP7, 6, pixels, [11]), # 4K
    Button(board.GP8, 8), # SELECT
    Button(board.GP9, 9), # START
    Button(board.GP28, 12), # HOME
    Button(board.GP17, 10), # L3
    Button(board.GP16, 11), # R3
    Button(board.GP18, 13) # TOUCH
]

# left, down, right, up
dpad = Directional(board.GP10, board.GP11, board.GP12, board.GP13, pixels, [0], [1], [2], [3])
ofs = OpenFightStick(usb_hid.devices)

while True:
    for button in buttons:
        if button.pressed():
            ofs.press_button(button)
            button.start_animation()
        else:
            ofs.release_button(button)
        button.animate()

    ofs.move_hat(dpad.dpad())
    dpad.animate()
    pixels.show()
