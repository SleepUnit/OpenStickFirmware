import digitalio
import board

class Button:
  def __init__(self, pin, num):
    self.num = num

    self._button = digitalio.DigitalInOut(pin)
    self._button.direction = digitalio.Direction.INPUT
    self._button.pull = digitalio.Pull.UP

  def pressed(self):
    return not self._button.value
    
class Directional:
  def __init__(self, left_pin, down_pin, right_pin, up_pin):
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
      return 1

    if right and down:
      return 3

    if right:
      return 2

    if left and up:
      return 7

    if left and down:
      return 5

    if left:
      return 6

    if up:
      return 0

    if down:
      return 4

    return 8