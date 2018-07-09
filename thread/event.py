#最简单的线程通信机制之一，一个线程通知事件，其他线程等待事件，set()默认为false clear()重置为false
#他就是一个简化版的condotion，他没有锁，无法使线程进入同步阻塞状态
import threading
import time

event = threading.Event()

def test():
    #等待事件，进入阻塞状态
    print('%s wait for event...' % threading.currentThread().getName())
    event.wait()

    #收到事件后进行操作
    print('%s recv event.' % threading.currentThread().getName())

t1 = threading.Thread(target=test)
t2 = threading.Thread(target=test)
t1.start()
t2.start()

time.sleep(2)

#我要发送事件通知了
print('the message is coming')
event.set()
