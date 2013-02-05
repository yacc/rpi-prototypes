#!/usr/bin/python3
##------------------------------------------------------------------------------
## Project   : Yuka
## Descriptio: test LED on RPi 1Hz to 25Hz
##------------------------------------------------------------------------------

import RPi.GPIO as GPIO
import os
from time import sleep

## Setup GPIO16 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
os.system("echo none >/sys/class/leds/led0/trigger");

for f in range(1, 25):
    d = float(1/f/2)

    for i in range(0, 5):
        GPIO.output(16, GPIO.LOW)
        sleep(d)
        GPIO.output(16, GPIO.HIGH)
        sleep(d)

    sleep(1)

## Restore trigger
os.system("echo mmc0 >/sys/class/leds/led0/trigger");
