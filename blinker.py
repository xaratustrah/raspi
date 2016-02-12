#!/usr/bin/env python
"""
A blinker for the Raspberry Pi

Xaratustrah
2016

"""

import time

try:
    import RPi.GPIO as gpio
except RuntimeError:
    print("""Error importing RPi.GPIO!  This is probably because you need superuser privileges.
                You can achieve this by using 'sudo' to run your script""")

LED = 31  # assign pin number

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(LED, gpio.OUT)

print('Blinker started. ctrl-c to abort.\n')
try:
    while True:
        gpio.output(31, gpio.HIGH)
        time.sleep(0.3)
        gpio.output(31, gpio.LOW)
        time.sleep(0.3)

except(EOFError, KeyboardInterrupt):
    print('\nUser input cancelled. Aborting...')
    gpio.output(31, gpio.LOW)

gpio.cleanup()
