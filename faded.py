import pwmio
import board

MAX_CYCLE = 2 ** 16

led = pwmio. PWMOut(board.D6)

while True:
    led.duty_cycle = int(MAX_CYCLE/2)
