import RPi.GPIO as GPIO
import cv2 as cv
import time
from movement import ServoControl

servo_1 = ServoControl(GPIO.BOARD, frequency=50, pin_number=16)
servo_2 = ServoControl(GPIO.BOARD, frequency=50, pin_number=18)

# some tests

servo_1.set_angle(90)
servo_2.set_angle(90)

print('Done')

GPIO.cleanup()