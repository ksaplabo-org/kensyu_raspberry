# インポート
import RPi.GPIO as GPIO
import time

# GPIO指定
PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
  while True:
    print('ON')
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(1)

    print('OFF')
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()