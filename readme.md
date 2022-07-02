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

## ここからモブプログラミングで行う  
## Iot Coreからモノの作成  
事前準備  
・踏み台サーバにログインし、ブラウザ(Chrome)を起動し  
  講師のアカウントでログインまでやっておく  
　→AWSのSSMを起動してもらう
・支店にあるRaspberry piに温湿度センサと液晶ディスプレイを接続しておく  
  (動作確認もしておく)  
・踏み台サーバで支店のラズベリーパイと接続し、コマンドを打てる状態にしておく  

Winsowsのリモートデスクトップで以下のアドレスに接続する  
```
EC2のIPアドレス（当日確認？）
```
ログインID,パスワードは以下の通り
```
ID: PW:
※teamsで送信  
```
アクセスしたら、ブラウザが立ち上がっているので、AWSのIoTCoreのコンソール画面に行く  

・「管理」から「全てのデバイス」→「モノ」を選択  
・ 右上の「モノを作成」を選択 
・「一つのモノを作成」を選択し、「次へ」を選択   
・「モノの名前」に任意の名前を入力（「air-condition-pi」）して「次へ」  
・「デバイス証明書」で「新しい証明書を自動生成 (推奨)」を選択して「次へ」  
・ 右上の「ポリシーを作成をクリック」→別ブラウザで立ち上がる  
・ 以下の情報でポリシーを作成する  
   ポリシー名：air-condition-policy
   ポリシー効果：許可
   ポリシーアクション：*
   ポリシーリソース：*
・ 元のブラウザに戻り作成したポリシーを選択して、「モノを作成」をクリック  
・ ここで表示される証明書、プライベートキー、パブリックキーをすべてダウンロードする。  
※ダウンロードは自分で行う!!
※ダウンロードした証明書類をラズパイのDownloadフォルダに移す！  
※その時のファイル名をコピーしてチームズで送る  
・ また、RaspberryPiが接続するための、IoTエンドポイントを以下の手順で確認する。
  （AWS IoTメニューの）「設定」をクリック
  「デバイスデータエンドポイント」にある「エンドポイント」をメモする。

次に、EC2のターミナルからMQTTクライアントのライブラリを取得する  
```
pip3 install paho-mqtt python-etcd
```
フォルダの位置を調整して、以下のコマンドでソースを編集する  
```
sudo nano aircondition.py
```

ここまでできたら、IotCoreのブラウザに戻り  
「テスト」からMQTTテストクライアントを選択  
トピックのフィルターに「topicAirCondition」を入れて
まずソースを実行、その後にサブスクライブを押す。

以上で1日目は終わり  
