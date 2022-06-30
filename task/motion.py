import RPi.GPIO as GPIO
import time

PIN_IN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN)

#main処理
try:
  while True:
    
    # 4ピンに入力があれば1
    if GPIO.input(PIN_IN) == 1:
        print("HIGH")
    else:
        print("LOW")

    time.sleep(1)

# 例外処理
except KeyboardInterrupt:
  GPIO.cleanup()