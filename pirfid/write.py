#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimleMFRC522

reader = SimpleMFRC522()

try:
    text = input('WRITE YOUR DATA!!!!:')
    print("NOW PLACE YOUR CARD OR I WILL KILL YOU!!")
    reader.write(text)
    print("OK... YOU'RE JUST LUCKY! Written.")
finnaly:
    GPIO.cleanup()