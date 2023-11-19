import board
import digitalio
import time

# Initialize the A3 pin as a digital output
led = digitalio.DigitalInOut(board.A3)
led.direction = digitalio.Direction.OUTPUT

while True:
    # Turn on the A3 pin
    led.value = True
    time.sleep(1)  # Wait for 1 second

    # Turn off the A3 pin
    led.value = False
    time.sleep(1)  # Wait for 1 second

