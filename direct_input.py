import usb_hid

class DirectInput:
  def __init__(self):
    self.report_id = 7
  
  def descriptor(self):
    return bytes((
      0x05, 0x01,	# USAGE_PAGE (Generic Desktop)
      0x09, 0x05,	# USAGE (Gamepad) - Very important for Switch
      0xa1, 0x01,	# COLLECTION (Application)
      0x85, 0xFF, # 7 [SET AT RUNTIME]

      # 16 Buttons
      0x05, 0x09,	#   USAGE_PAGE (Button)
      0x19, 0x01,	#   USAGE_MINIMUM (Button 1)
      0x29, 0x10,	#   USAGE_MAXIMUM (Button 16)
      0x15, 0x00,	#   LOGICAL_MINIMUM (0)
      0x25, 0x01,	#   LOGICAL_MAXIMUM (1)
      0x75, 0x01,	#   REPORT_SIZE (1)
      0x95, 0x10,	#   REPORT_COUNT (16)
      0x55, 0x00,	#   UNIT_EXPONENT (0)
      0x65, 0x00,	#   UNIT (None)
      0x81, 0x02,	#   INPUT (Data,Var,Abs)

      # One Hat switches (8 Positions)
      0x05, 0x01,	#   USAGE_PAGE (Generic Desktop)
      0x09, 0x39,	#   USAGE (Hat switch)
      0x15, 0x00,	#   LOGICAL_MINIMUM (0)
      0x25, 0x07,	#   LOGICAL_MAXIMUM (7)
      0x35, 0x00,	#   PHYSICAL_MINIMUM (0)
      0x46, 0x3B, 0x01,	      #   PHYSICAL_MAXIMUM (315)
      0x65, 0x14,	#   UNIT (Eng Rot:Angular Pos)
      0x75, 0x04,	#   REPORT_SIZE (4)
      0x95, 0x01,	#   REPORT_COUNT (1)
      0x81, 0x02,	#   INPUT (Data,Var,Abs)

      0x65, 0x00,
      0x95, 0x01,
      0x81, 0x01,

      # X, Y, and Z Axis
      0x15, 0x00,	#   LOGICAL_MINIMUM (0)
      0x26, 0xff, 0x00,	      #   LOGICAL_MAXIMUM (255)
      0x75, 0x08,	#   REPORT_SIZE (8)
      0x09, 0x01,	#   USAGE (Pointer)
      0xA1, 0x00,	#   COLLECTION (Physical)
      0x09, 0x30,	#     USAGE (x)
      0x09, 0x31,	#     USAGE (y)
      0x09, 0x32,	#     USAGE (z)
      0x09, 0x35,	#     USAGE (rz)
      0x95, 0x04,	#     REPORT_COUNT (4)
      0x81, 0x02,	#     INPUT (Data,Var,Abs)
      0xc0,	#   END_COLLECTION
      0xc0	# END_COLLECTION
    ))
  
  def device(self):
    return usb_hid.Device(
      report_descriptor = self.descriptor(),
      usage_page = 0x1,
      usage = 0x5,
      in_report_length = 7,
      out_report_length = 1,
      report_id_index = self.report_id,
    )


