import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 02

Motor1B = 03

Motor1E = 04

GPIO.setup(Motor1A, GPIO.OUT)

GPIO.setup(Motor1B, GPIO.OUT)

GPIO.setup(Motor1E, GPIO.OUT)

print "Motor going to Start"

GPIO.output(Motor1A, GPIO.HIGH)  # to run motor in clockwise direction

GPIO.output(Motor1B, GPIO.LOW)  # put it high to rotate motor in anti-clockwise direction

GPIO.output(Motor1E, GPIO.HIGH)  # Should be always high to start motor

sleep(5)

print "Stopping motor"

GPIO.output(Motor1E, GPIO.LOW)  # to stop the motor

GPIO.cleanup()
