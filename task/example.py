import RPi.GPIO as GPIO
import dht11				#温湿度センサを使用するためのライブラリ
import time
import datetime

# GPIOを使用するための宣言
GPIO.setwarnings(True)	# 警告を表示するかしないかの設定(Trueは表示する)
GPIO.setmode(GPIO.BCM)

# 温湿度センサ(DHT11)で14ピンを使うよという宣言
instance = dht11.DHT11(pin=14)

# ループ処理
try:
	while True:
		# 温度と湿度の取得
		result = instance.read()
		# 温度と湿度が取得できたことを確認
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %-3.1f C" % result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)

		time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()