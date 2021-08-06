import board
import usb_hid
from ofs import OpenFightStick
from controls import Button, Directional

buttons = [
    Button(board.GP0, 0), # 1P 
    Button(board.GP1, 3), # 2P
    Button(board.GP2, 5), # 3P
    Button(board.GP3, 4), # 4P
    Button(board.GP4, 1), # 1K
    Button(board.GP5, 2), # 2K
    Button(board.GP6, 7), # 3K
    Button(board.GP7, 6), # 4K
    Button(board.GP8, 8), # SELECT
    Button(board.GP9, 9), # START
    Button(board.GP28, 12), # HOME
    Button(board.GP17, 10), # L3
    Button(board.GP16, 11), # R3
    Button(board.GP18, 13) # TOUCH
]

# left, down, right, up
dpad = Directional(board.GP10, board.GP11, board.GP12, board.GP13)

ofs = OpenFightStick(usb_hid.devices)

while True:
    pressed = list(map(lambda b: b.num + 1, filter(lambda b: b.pressed(), buttons)))
    unpressed = list(map(lambda b: b.num + 1, filter(lambda b: not b.pressed(), buttons)))
 
    ofs.press_buttons(*pressed)
    ofs.release_buttons(*unpressed)

    ofs.move_hat(dpad.dpad())