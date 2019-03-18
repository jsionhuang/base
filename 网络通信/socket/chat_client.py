import threading
import socket

name = input('input you name')
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#1.获得tcp的套接字
s.connect(('127.0.0.1',9999))#2.与服务端简历链接

def getresponse():
    while True:
        try:
            data = s.recv(1024)#3.建立链接后，接受服务端的数据
            print(data.decode(encoding = 'utf-8'))
        except:
            break

t = threading.Thread(target=getresponse)
t.start()
while True:
    st = input()
    if st == 'exit':
        s.send(st)
        s.close()#当要退出的时候关闭  套接字
        break
    else:
        s.send((name+':'+st).encode(encoding='utf-8'))