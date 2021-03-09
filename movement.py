import RPi.GPIO as GPIO
import time


class ServoControl:
    def __init__(self, set_mode, frequency, pin_number):
        self.FREQUENCY = frequency
        self.PIN = pin_number

        GPIO.setmode(set_mode)
        GPIO.setup(self.PIN, GPIO.OUT)
        self.pwm = GPIO.PWM(self.PIN, self.FREQUENCY)
        self.pwm.start(0)

    def set_angle(self, angle):
        duty = angle / 18 + 2

        GPIO.output(self.PIN, True)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(self.PIN, False)
        self.pwm.ChangeDutyCycle(0)
