#!/usr/bin/env python
"""
A blinker for the Raspberry Pi

Xaratustrah
2016

"""

import time
import RPi.GPIO as gpio

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
