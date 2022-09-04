#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimleMFRC522

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print(id)
    print(text)
finnaly:
    GPIO.cleanup()