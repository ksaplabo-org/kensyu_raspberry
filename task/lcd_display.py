import RPi.GPIO as GPIO
import dht11
import time
import datetime
import board
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

display = SSD1306_I2C(128, 64, board.I2C(), addr=0x3C)

FONT_SANS_12 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,12)

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

# メイン
try:
    while True:
        tm = datetime.datetime.now()
        tmstr = "{0:%Y-%m-%d %H:%M:%S}".format(tm)
        result = instance.read()

        if result.is_valid():
            temp_val = result.temperature
            humi_val = result.humidity

        print("datetime:" + tmstr + " Temperature: %-3.1f C" % temp_val + " Humidity: %-3.1f %%" % humi_val)

        # draw image
        img = Image.new("1",(display.width, display.height))
        draw = ImageDraw.Draw(img)
        draw.text((0,0),'時刻 ' + tm.strftime('%H:%M:%S'),font=FONT_SANS_12,fill=1)        

        display.image(img)
        display.show()

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()