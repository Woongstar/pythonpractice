import keyboard
from PIL import  ImageGrab
import time
def screenshot():
    current_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("imgage{}.png".format(current_time))

keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc")