import RPi.GPIO as GPIO
import time

PIN1 = 20
PIN2 = 16
PIN3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)

try:
    while(True):
        GPIO.output(PIN1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PIN2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PIN3, GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(PIN1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(PIN2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(PIN3, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()