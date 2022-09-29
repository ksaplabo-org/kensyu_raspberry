import RPi.GPIO as GPIO
import time

PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    while(True):
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(0.001)

        GPIO.output(PIN, GPIO.LOW)
        time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()
