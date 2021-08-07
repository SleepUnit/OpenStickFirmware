import board
import usb_hid
import neopixel
from ofs import OpenFightStick
from controls import Button, Directional
from leds import Leds
from config import config

# Setup LEDs if the appropriate configuration exists. Otherwise,
# make sure we set pixels so that we don't have to do bootleg 
# Python undefined checking everywhere.
pixels = None

if config.get('led_pin') and config.get('led_num'):
    pixels = neopixel.NeoPixel(config.get('led_pin'), config.get('led_num'), brightness=0.3, auto_write=False)

# Add buttons and their corresponding LEDs, if they exist in our config.
def add_button(pin, hid_num, leds):
    if config.get(pin):
        buttons.append(Button(config.get(pin), hid_num, pixels, config.get(leds, [])))

buttons = []
add_button('1p_pin', 0, '1p_leds')
add_button('2p_pin', 3, '2p_leds')
add_button('3p_pin', 5, '3p_leds')
add_button('4p_pin', 4, '4p_leds')
add_button('1k_pin', 1, '1k_leds')
add_button('2k_pin', 2, '2k_leds')
add_button('3k_pin', 7, '3k_leds')
add_button('4k_pin', 6, '4k_leds')
add_button('select_pin', 8, 'select_leds')
add_button('start_pin', 9, 'start_leds')
add_button('home_pin', 12, 'home_leds')
add_button('l3_pin', 10, 'l3_leds')
add_button('r3_pin', 11, 'r3_leds')
add_button('touch_pin', 13, 'touch_leds')

# left, down, right, up
dpad = Directional(config.get('left_pin'), config.get('down_pin'), config.get('right_pin'), config.get('up_pin'), pixels, config.get('left_leds', []), config.get('down_leds', []), config.get('right_leds', []), config.get('up_leds', []))
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
    if pixels:
        pixels.show()
