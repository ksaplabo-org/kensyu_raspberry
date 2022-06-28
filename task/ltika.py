# インポート
import RPi.GPIO as GPIO
import time

# GPIO指定
PIN = 21
# GPIOを使用するための宣言
GPIO.setmode(GPIO.BCM)      #GPIOで使用する宣言
GPIO.setup(PIN, GPIO.OUT)   #21ピンを出力として利用する

# main処理
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