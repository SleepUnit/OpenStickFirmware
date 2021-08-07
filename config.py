import board

config = {
  # Have LEDs? Specify the pin and number of LEDs. These should be WS2812b or
  # other NeoPixel style LEDs. Comment these lines out otherwise.
  "led_pin": board.GP14,
  "led_num": 16,

  # Action Buttons. Specify the pin for any buttons your controller has. Comment out
  # any buttons you don't have. If your controller has LEDs for each button, also
  # provide the index of those. This may be one or many depending on how much you
  # live that RGB life.
  "1p_pin": board.GP0,
  "1p_leds": [4],
  "2p_pin": board.GP1,
  "2p_leds": [5],
  "3p_pin": board.GP2,
  "3p_leds": [6],
  "4p_pin": board.GP3,
  "4p_leds": [7],

  "1k_pin": board.GP4,
  "1k_leds": [8],
  "2k_pin": board.GP5,
  "2k_leds": [9],
  "3k_pin": board.GP6,
  "3k_leds": [10],
  "4k_pin": board.GP7,
  "4k_leds": [11],

  "select_pin": board.GP8,
  # "select_leds": [12],
  "start_pin": board.GP9,
  # "start_leds": [9],
  "home_pin": board.GP28,
  # "home_leds": [10],
  "l3_pin": board.GP17,
  # "l3_leds": [11],
  "r3_pin": board.GP16,
  # "r3_leds": [11],
  "touch_pin": board.GP18,
  # "touch_leds": [11],

  # Directional Buttons. More of the same. Currently, these pins are required. That's
  # probably shortsighted on my part, but it is what it is.
  "left_pin": board.GP10,
  "left_leds": [0],
  "down_pin": board.GP11,
  "down_leds": [1],
  "right_pin": board.GP12,
  "right_leds": [2],
  "up_pin": board.GP13,
  "up_leds": [3]
}