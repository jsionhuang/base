#开发CS架构软件
#应用层，传输层，网络层，数据链路层
'''
1.获得tcp或ucp的套接字
2.为套接字绑定地址
3.监听套接字
4.accept接受来自客户端的套接字链接
5.rec接受客户端发来的信息
6.send发送信息
'''
import socket
import threading

def dealrequest(accep,addr):
    print(addr)
    print('is oline')
    while True:
        try:
            data = accep.recv(1024)#5.接受客户端发来的消息
        except:
            socket_set.remove(accep)
            print(addr)
            print('is downing')
            break
        if data == 'exit' or not data:
            socket_set.remove(accep)
            accep.close()
            print(addr)
            print('is downing')
        else:
            list1 = []
            for i in socket_set:
                if i != accep:
                    list1.append(i)
            for i in list1:
                i.send(data)#发送客户端的消息
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#1.服务器获得套接字
socket_set = set()#用来保存socket对象
sock.bind(('127.0.0.1',9999))#2.套接字绑定地址
sock.listen(5)#3.套接字弄好监听
print("server is waiting connect....")
while True:
    accep,addr = sock.accept()#4.接受客户端的链接
    socket_set.add(accep)
    t = threading.Thread(target=dealrequest,args=(accep,addr))
    t.start()




#客户端
'''
1.创建客户套接字
2.connect尝试链接
3.发送send 或者rec接受套接字
4.close关闭客户套接字
'''
