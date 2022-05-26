import RPi.GPIO as GPIO
import time
import datetime
import asyncio
import board
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

display = SSD1306_I2C(128, 64, board.I2C(), addr=0x3C)

FONT_SANS_12 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,12)

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# Publish Loop
async def pub_loop():
    while True:
        tm = datetime.datetime.now()
        tmstr = "{0:%Y-%m-%d %H:%M:%S}".format(tm)

        print("datetime:" + tmstr)

        # draw image
        img = Image.new("1",(display.width, display.height))
        draw = ImageDraw.Draw(img)
        draw.text((0,0),'時刻 ' + tm.strftime('%H:%M:%S'),font=FONT_SANS_12,fill=1)

        display.image(img)
        display.show()

        time.sleep(1)

# Main Procedure
try:
    if __name__ == '__main__':
        # Start Publish Loop 
        loop = asyncio.get_event_loop()
        loop.run_until_complete(pub_loop())


except KeyboardInterrupt:
    GPIO.cleanup()