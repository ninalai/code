import time
import digitalio
import board

led = digitalio.DigitalInOut(board.D1)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while true:
    if button.value == TRUE:
        led.value = True
    else:
        led.value = False
    time.sleep(0.1)
