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
