# Copyright (c) 2021 Jonathan Barket
# Copyright (c) 2018 Dan Halbert for Adafruit Industries 

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from adafruit_hid.keyboard import find_device
import usb_hid
import struct
import time

class OpenFightStick:
    def __init__(self, devices):
        self._device = find_device(devices, usage_page=0x1, usage=0x05)

        # report[0] buttons 1-8 (LSB is button 1)
        # report[1] buttons 9-16
        # report[2] hat 0-8
        # report[3] joystick 0 x: -127 to 127
        # report[4] joystick 0 y: -127 to 127
        # report[5] joystick 1 x: -127 to 127
        # report[6] joystick 1 y: -127 to 127
        self._report = bytearray(7)

        # Remember the last report as well, so we can avoid sending
        # duplicate reports.
        self._last_report = bytearray(7)

        # Store settings separately before putting into report. Saves code
        # especially for buttons.
        self._buttons_state = 0
        self._hat_position = 8
        self._joy_x = 0
        self._joy_y = 0
        self._joy_z = 0
        self._joy_r_z = 0

        # Send an initial report to test if HID device is ready.
        # If not, wait a bit and try once more.
        try:
            self.reset_all()
        except OSError:
            time.sleep(1)
            self.reset_all()

    def press_button(self, button):
        self._buttons_state |= 1 << button.num
        self._send()

    def release_button(self, button):
        self._buttons_state &= ~(1 << button.num)
        self._send()

    def move_hat(self, direction):
      """ DPad is interpreted as a hat. Values are 0-7 where N is 0, and the
      directions move clockwise. 8 is centered. """
      self._hat_position = direction
      self._send()

    def move_joysticks(self, x=None, y=None, z=None, r_z=None):
        if x is not None:
            self._joy_x = x
        if y is not None:
            self._joy_y = y
        if z is not None:
            self._joy_z = z
        if r_z is not None:
            self._joy_r_z = r_z
        self._send()

    def reset_all(self):
        """Return the fightstick to a neutral state"""
        self._buttons_state = 0
        self._hat_position = 8
        self._joy_x = 0
        self._joy_y = 0
        self._joy_z = 0
        self._joy_r_z = 0
        self._send(always=True)

    def _send(self, always=False):
        """Send a report with all the existing settings.
        If ``always`` is ``False`` (the default), send only if there have been changes.
        """
        struct.pack_into(
            "<HBbbbb",
            self._report,
            0,
            self._buttons_state,
            self._hat_position,
            self._joy_x,
            self._joy_y,
            self._joy_z,
            self._joy_r_z,
        )

        if always or self._last_report != self._report:
            self._device.send_report(self._report)
            self._last_report[:] = self._report

