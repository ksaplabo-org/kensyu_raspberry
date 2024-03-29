import RPi.GPIO as GPIO
import dht11 
import time
import datetime
import paho.mqtt.client
import json
import asyncio
import ssl
import board
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# ディスプレイの初期処理
i2c = board.I2C()
display = SSD1306_I2C(128, 64, board.I2C(), addr=0x3C)
FONT_SANS_12 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,12)
FONT_SANS_18 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,18)

# GPIOの初期化
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# MQTT通信で使用する定数定義 ※ここを変更してください
AWSIoT_ENDPOINT = "alij9rhkrwgll-ats.iot.ap-northeast-1.amazonaws.com"
MQTT_PORT = 8883
MQTT_TOPIC_PUB = "topicAirCondition"
MQTT_TOPIC_SUB = "topicAirConditionSub"
MQTT_ROOTCA = "/home/pi/Desktop/AmazonRootCA1.pem"
MQTT_CERT = "/home/pi/Desktop/30798132e0e9b6f7f52e181076f378c530c33a0741d6cbd5329b5a4bf277fd14-certificate.pem.crt"
MQTT_PRIKEY = "/home/pi/Desktop/30798132e0e9b6f7f52e181076f378c530c33a0741d6cbd5329b5a4bf277fd14-private.pem.key"

# 温湿度センサ(DHT11)で14ピンを使うよという宣言
instance = dht11.DHT11(pin=14)

# ループ処理
async def pub_loop():
    temp_val=0
    humi_val=0
    count=0

    while True:
        tm = datetime.datetime.now()
        tmstr = "{0:%Y-%m-%d %H:%M:%S}".format(tm)
        result = instance.read()
        if result.is_valid():
            temp_val = result.temperature
            humi_val = result.humidity

        print("datetime:" + tmstr + " Temperature: %.1f C" % temp_val + " Humidity: %.1f %%" % humi_val)

		# 送信するJSONデータの作成
        json_msg = json.dumps({"GetDateTime": tmstr, "Temperature": temp_val,"Humidity":humi_val})

        # 画像データの作成
        img = Image.new("1",(display.width, display.height))
        draw = ImageDraw.Draw(img)
        draw.text((0,0),'時刻 ' + tm.strftime('%H:%M:%S'),font=FONT_SANS_12,fill=1)
        draw.text((0,16),'温度 {0:.1f}℃ 湿度 {1:.1f}%'.format(float(temp_val) ,float(humi_val)) ,font=FONT_SANS_12,fill=1)

        # ディスプレイに表示
        display.image(img)
        display.show()

		# 10秒に1回パブリッシュを行う
        if count==10:
            client.publish(MQTT_TOPIC_PUB ,json_msg)
            count=0
        
        time.sleep(1)
        count=count+1

# Main処理
if __name__ == '__main__':
    # Mqttクライアントの初期化
    client = paho.mqtt.client.Client()
    
    # Mqttクライアントの接続設定
    client.tls_set(MQTT_ROOTCA, certfile=MQTT_CERT, keyfile=MQTT_PRIKEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    # MQTTブローカーとの接続
    client.connect(AWSIoT_ENDPOINT, port=MQTT_PORT, keepalive=60)

    # 処理開始
    client.loop_start()

    # ループスタート
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pub_loop())
