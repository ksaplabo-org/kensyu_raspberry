import RPi.GPIO as GPIO
import time

PIN_IN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN)

#メイン
try:
  #繰り返す
  while True:
    #現在のPIN状態を標準出力
    print(GPIO.input(PIN_IN))

    if GPIO.input(PIN_IN) == 1:
        print("HIGH")
    else:
        print("LOW")

    time.sleep(1)

# 終了時
except KeyboardInterrupt:
  GPIO.cleanup()