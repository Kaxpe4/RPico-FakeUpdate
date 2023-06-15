import usb_hid
from adafruit_hid.mouse import Mouse
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid. devices)
layout = KeyboardLayoutUS(kbd)
LEFT_GUI = 0xE3
GUI = LEFT_GUI
WINDOWS = GUI
ENTER = 0x28
RETURN = ENTER
F11 = 0x44

kbd.send(Keycode.GUI, Keycode.R)
time.sleep(0.5)
layout.write("chrome.exe")
time.sleep(0.5)
kbd.send(Keycode.RETURN)
time.sleep(1)
layout.write("fakeupdate.net/win10ue/")
time.sleep(0.5)
kbd.send(Keycode.RETURN)
time.sleep(0.5)
kbd.send(Keycode.F11)


