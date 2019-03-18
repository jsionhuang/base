import socket
import threading
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',8888))
sk.listen(5)
def deal_request(conn,addr):
    conn.send('欢迎致电10086，0转人工服务'.encode(encoding='utf-8'))
    flag = True
    while flag:
        tmp = conn.recv(1024)
        data = tmp.decode(encoding = 'utf-8')
        if data == 'exit':
            flag = False
        elif data == '0':
            conn.send('进入人工服务'.encode(encoding='utf-8'))
        else:
            conn.send('请重新输入'.encode(encoding='utf-8'))
    conn.close()
while True:
    conn,addr = sk.accept()
    t = threading.Thread(target=deal_request,args=(conn,addr))
    t.start()