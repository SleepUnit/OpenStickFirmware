import digitalio
import board
from leds import Leds

class Button:
  def __init__(self, pin, num, pixels = None, pixel_group = []):
    self.num = num
    self.pixels = pixels

    self._button = digitalio.DigitalInOut(pin)
    self._button.direction = digitalio.Direction.INPUT
    self._button.pull = digitalio.Pull.UP

    self.leds = None

    if pixels and len(pixel_group) > 0:
      self.leds = Leds(pixels, pixel_group)

  def pressed(self):
    return not self._button.value

  def start_animation(self):
    if self.leds:
      self.leds.start("Wheel")

  def animate(self):
    if self.leds:
      self.leds.animate()


class Directional:
  def __init__(self, left_pin, down_pin, right_pin, up_pin, pixels, left_pixel_group, down_pixel_group, right_pixel_group, up_pixel_group):
    self.left_leds = None
    self.down_leds = None
    self.right_leds = None
    self.up_leds = None

    if pixels:
      if len(left_pixel_group) > 0:
        self.left_leds = Leds(pixels, left_pixel_group)
      if len(down_pixel_group) > 0:
        self.down_leds = Leds(pixels, down_pixel_group)
      if len(right_pixel_group) > 0:
        self.right_leds = Leds(pixels, right_pixel_group)
      if len(up_pixel_group) > 0:
        self.up_leds = Leds(pixels, up_pixel_group)
    
    self._left = digitalio.DigitalInOut(left_pin)
    self._left.direction = digitalio.Direction.INPUT
    self._left.pull = digitalio.Pull.UP

    self._down = digitalio.DigitalInOut(down_pin)
    self._down.direction = digitalio.Direction.INPUT
    self._down.pull = digitalio.Pull.UP

    self._right = digitalio.DigitalInOut(right_pin)
    self._right.direction = digitalio.Direction.INPUT
    self._right.pull = digitalio.Pull.UP

    self._up = digitalio.DigitalInOut(up_pin)
    self._up.direction = digitalio.Direction.INPUT
    self._up.pull = digitalio.Pull.UP


  def animate(self):
    if self.left_leds:
      self.left_leds.animate()
    if self.down_leds:
      self.down_leds.animate()
    if self.right_leds:
      self.right_leds.animate()
    if self.up_leds:
      self.up_leds.animate()

  def dpad(self):
    return self._full_neutral_clean(not self._left.value, not self._down.value, not self._right.value, not self._up.value)

  def _full_neutral_clean(self, left = False, down = False, right = False, up = False):
    if up and down:
      up = False
      down = False

    if left and right:
      left = False
      right = False

    return self._post_clean(left, down, right, up)

  def _post_clean(self, left = False, down = False, right = False, up = False):
    if right and up:
      if self.right_leds:
        self.right_leds.start("Wheel")
      if self.up_leds:
        self.up_leds.start("Wheel")
      return 1

    if right and down:
      if self.right_leds:
        self.right_leds.start("Wheel")
      if self.down_leds:
        self.down_leds.start("Wheel")
      return 3

    if right:
      if self.right_leds:
        self.right_leds.start("Wheel")
      return 2

    if left and up:
      if self.left_leds:
        self.left_leds.start("Wheel")
      if self.up_leds:
        self.up_leds.start("Wheel")
      return 7

    if left and down:
      if self.left_leds:
        self.left_leds.start("Wheel")
      if self.down_leds:
        self.down_leds.start("Wheel")
      return 5

    if left:
      if self.left_leds:
        self.left_leds.start("Wheel")
      return 6

    if up:
      if self.up_leds:
        self.up_leds.start("Wheel")
      return 0

    if down:
      if self.down_leds:
        self.down_leds.start("Wheel")
      return 4

    return 8