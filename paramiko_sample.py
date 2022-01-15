import json
import os

import paramiko 

def main():
    #ホスト情報が格納されているhostinfo.jsonを読み取る
    json_file_reader=open('hostinfo.json','r')
    json_load=json.load(json_file_reader)

    ip=json_load['IP']
    user=json_load['USER']
    secret_key=json_load['SECRET_KEY_PATH']

    client=paramiko.SSHClient()
    client.set_missing_host_key_policy=(paramiko.WarningPolicy)
    
    # マシン上のknouwn_hostsをロードする
    # ロードしないと以下のエラーが発生
    # aramiko.ssh_exception.SSHException: Server <ホスト名> not found in known_hosts
    client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    
    # パスワードで接続する際は引数に passphraseを設定
    client.connect(
        hostname=ip,
        username=user,
        key_filename=secret_key,
        timeout=5.0
    )
    
    #実行するコマンドを指定
    cmd=''

    stdin, stdout, stderr=client.exec_command(cmd)

    # 実行結果を出力
    print('==========out==========')
    cmd_result = ''
    for line in stdout:
        cmd_result += line
    print(cmd_result)

    print('==========error==========')
    cmd_result = ''
    for line in stderr:
        cmd_result += line
    if cmd_result is not '':
        print(cmd_result)

    # sshの切断
    client.close()
    del client, stdin, stdout, stderr


if __name__ == "__main__":
    main()