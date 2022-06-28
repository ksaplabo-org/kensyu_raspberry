import RPi.GPIO as GPIO
import dht11                                    #温湿度センサを利用するためのライブラリ
import time
import datetime
import asyncio
import board
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# ディスプレイの初期処理
display = SSD1306_I2C(128, 64, board.I2C(), addr=0x3C)
FONT_SANS_12 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,12)

# GPIOの初期化
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# 温湿度センサ(DHT11)で14ピンを使うよという宣言
instance = dht11.DHT11(pin=14)

# ループ処理
async def pub_loop():
    # 温度と湿度
    temp_val=0
    humi_val=0
    # 無限ループ
    while True:
        # 現在時刻の取得
        tm = datetime.datetime.now()
        # 時刻のフォーマット設定
        tmstr = "{0:%Y-%m-%d %H:%M:%S}".format(tm)
        # 温度と湿度の取得
        result = instance.read()
        # 温度と湿度が取得できたことを確認
        if result.is_valid():
            temp_val = result.temperature
            humi_val = result.humidity

        # ターミナルに出力
        print("datetime:" + tmstr + " Temperature: %.1f C" % temp_val + " Humidity: %.1f %%" % humi_val)

        # 画像データの作成
        img = Image.new("1",(display.width, display.height))
        # 画像に描画するためのオブジェクト宣言
        draw = ImageDraw.Draw(img)
        # テキストを描画
        draw.text((0,0),'時刻 ' + tm.strftime('%H:%M:%S'),font=FONT_SANS_12,fill=1)
        draw.text((0,16),'温度 {0:.1f}℃ 湿度 {1:.1f}%'.format(float(temp_val) ,float(humi_val)) ,font=FONT_SANS_12,fill=1)

        # ディスプレイに表示
        display.image(img)
        display.show()

        # 1秒待機
        time.sleep(1)

# Main Procedure
if __name__ == '__main__':

    try:
        # ループスタート 
        loop = asyncio.get_event_loop()
        loop.run_until_complete(pub_loop())

    except KeyboardInterrupt:
        GPIO.cleanup()
        # ディスプレイの表示を削除
        display.fill(0)
        display.show()
