# paramiko
paramikoのサンプルスクリプト  
ホストへSSHで接続しコマンドをリモートで実行する。  

# 使用方法  
- 必要なライブラリのインストール  
'''shell
pip install requirements.txt
'''  
  
- 以下のような設定用jsonファイルの作成  
'''json
{
    "IP":"your host ip address",
    "USER":"login username",
    "SECRET_KEY_PATH":"your secret key path"
}
'''  
  
- スクリプト内のコマンドを指定  
'''python
cmd='ls -l'
'''  
  
- スクリプトを実行  
'''shell
python3 paramiko_sample.py  
'''  
