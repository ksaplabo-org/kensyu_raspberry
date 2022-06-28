# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# 今回使用するGPIO番号
PIN = 21

# GPIOを使用するための宣言
GPIO.setmode(GPIO.BCM)      # GPIOで使用する宣言
GPIO.setup(PIN, GPIO.OUT)   # 21ピンを出力として利用する

# main処理
try:
  while True:

    # ターミナルにONと出力
    print('ON')
    # 21ピンに電気を流す
    GPIO.output(PIN, GPIO.HIGH)
    # 1秒待機
    time.sleep(1)

    print('OFF')
    # 21ピンに流している電気を止める
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(1)

# 例外処理
except KeyboardInterrupt:
  # ピンの状態を初期化する
  GPIO.cleanup()