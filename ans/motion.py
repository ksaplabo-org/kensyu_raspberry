import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

try:
  while True:
    print(GPIO.input(17))

    if GPIO.input(17) == 1:
      GPIO.output(18, GPIO.HIGH)
    else:
      GPIO.output(18, GPIO.LOW)

    time.sleep(0.1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()
