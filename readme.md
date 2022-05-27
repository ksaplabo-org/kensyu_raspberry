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
sudo git clone https://github.com/szazo/DHT11_Python.git
```
配線を組めたら以下を実行  
```
python3 ./DHT11_Python/example.py
```

## DHT11ライブラリの移動
以下の順番でコマンドを実行する
・サンプルをコピー
```
sudo cp ./DHT11_Python/example.py ./aircond.py
```
・gitファイいる削除
```
cd DHT11_Python
```
```
rm -rf .git
```
・ライブラリ本体のフォルダをひとつ上に移動
```
cd ..
```
```
sudo mv -f ./DHT11_Python/dht11/ ./dht11
```
・不要フォルダの削除
```
sudo rm -rf ./DHT11_Python
```

## 温湿度センサの情報をディスプレイに表示  

SSD1306用のドライバのインストール  
```
pip3 install adafruit-circuitpython-ssd1306 
```
boardモジュールのインストール  
```
pip3 install board
```
これだけだとまだエラーが出るので、こちらを試して見る  
```
pip3 install adafruit-blinka
```
```
python3 -m pip install --force-reinstall adafruit-blinka
```
```
sudo apt-get install fonts-noto
```
最後のやつが15分くらいかかった

配線を組めたら、配線が正しいか以下のコマンドで確認する  
```
i2cdetect -y 1
```
以下のコマンドで実行する  
```
python3 lcd_display.py
```


