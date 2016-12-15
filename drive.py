#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

DA = 18
DB = 23
TA = 24
TB = 25
ENABLE = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(DA, GPIO.OUT)
GPIO.setup(DB, GPIO.OUT)
GPIO.setup(TA, GPIO.OUT)
GPIO.setup(TB, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)

GPIO.output(ENABLE, GPIO.HIGH)
GPIO.output(DA, GPIO.LOW)
GPIO.output(DB, GPIO.LOW)
GPIO.output(TA, GPIO.LOW)
GPIO.output(TB, GPIO.LOW)

def forward():
	GPIO.output(DA, GPIO.HIGH)
	GPIO.output(DB, GPIO.LOW)
	
def backward():
	GPIO.output(DA, GPIO.LOW)
	GPIO.output(DB, GPIO.HIGH)

def right():
	GPIO.output(TA, GPIO.HIGH)
	GPIO.output(TB, GPIO.LOW)

def left():
	GPIO.output(TA, GPIO.LOW)
	GPIO.output(TB, GPIO.HIGH)

try:
	while True:
		inp = input("drive:")
		if inp == 'q':
			break
		elif inp == 'w':
			forward()
		elif inp == 's':
			backward()
		elif inp == 'a':
			left()
		elif inp == 'd':
			right()
			

finally:
	GPIO.cleanup()
