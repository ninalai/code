import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

RED=(255, 0, 0)
YELLOW = (255, 150, 0)

def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

while True:
    color_chase(RED, 0.5)
    color_chase(YELLOW, 0.5)
