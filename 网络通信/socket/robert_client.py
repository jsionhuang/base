import socket
import threading
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1',8888))
sk.settimeout(5)
def delresponse():
    while True:
        try:
            data = sk.recv(1024)
            print(data.decode(encoding = 'utf-8'))
        except:
            break
t = threading.Thread(target=delresponse)
t.start()
while True:
    inp = input('请输入数字')
    if inp == 'exit':
        sk.close()
        break
    else:
        sk.send(inp.encode(encoding='utf=8'))
