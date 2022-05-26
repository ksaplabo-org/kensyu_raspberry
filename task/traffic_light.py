# 同時点灯
# 順番に点灯
# おまかせ。

# インポート
import RPi.GPIO as GPIO
import time

# GPIO指定


# pythonにおける関数定義や条件分岐の例
#def hoge_print(num_range):
#  for num in range(num_range):
#    if num % 2 == 0 :
#      print(num)
#    elif num % 3 == 0 :
#      print(-num)
#    else :
#      print('hoge')

# メイン
try:
  #hoge_print(10)

# 終了時
except KeyboardInterrupt:
  GPIO.cleanup()