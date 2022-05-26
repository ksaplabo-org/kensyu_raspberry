# 全国研修用の作業フォルダ  

実習用のソースを全部取得  
```
git clone https://github.com/ksaplabo-org/kensyu_raspberry.git  
```  
最初の作業フォルダに移動  
```
cd kensyu_raspberry/task
```

## Lチカ  
配線図通り配線出来たら以下を実行  
```
python3 ltika.py
```

## 信号機の作成  
配線を組めたら以下を実行し、ファイルの編集を行う  
```
sudo nano traffic_light.py
```
編集したファイルを実行するには以下のコマンドを実行  
```
python3 traffic_light.py
```

## 人感センサの利用  
配線図通り配線出来たら以下を実行  
```
python3 motion.py
```

## スピーカの利用  
配線を組めたら以下を実行し、ファイルの編集を行う  
```
sudo nano speaker.py
```
ソースのヒントはLチカのソースが参考になるため、画面共有でＬチカのソースを見せる  
編集したファイルを実行するには以下のコマンドを実行  
```
python3 speaker.py
```

## アラームシステムの作成  
配線を組めたら以下を実行し、ファイルの編集を行う  
```
sudo nano alert.py
```
編集したファイルを実行するには以下のコマンドを実行  
```
python3 alert.py
```

## 温湿度センサの利用  
dht11のライブラリを取得  
```
pip install dht11
```
配線を組めたら以下を実行  
```
python3 dht11.py
```

## 温湿度センサの情報をディスプレイに表示  
配線を組めたら、配線が正しいか以下のコマンドで確認する  
```
i2cdetect -y 1
```
以下のコマンドで実行する  
```
python3 lcd_display.py
```