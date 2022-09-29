import RPi.GPIO as GPIO
import time

GPIO_motion = 17
GPIO_speaker = 26

def alert(self):
    alert = GPIO.PWM(GPIO_speaker, 1000)
    alert.start(50)
    time.sleep(3)
    alert.stop()

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_motion, GPIO.IN)
GPIO.setup(GPIO_speaker, GPIO.OUT)
GPIO.add_event_detect(GPIO_motion, GPIO.RISING, callback=alert, bouncetime=2000)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
