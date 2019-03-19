import threading
import time

num = 0
def no_lock(arg):
    global num
    time.sleep(1)
    num +=1
    print(num)
for i in range(0,100):
    t = threading.Thread(group=None,name=None,target=no_lock,args=(i,))
    t.start()
print('no lock 线程 is over')

rlock = threading.RLock()
def is_lock(arg):
    #开启acquire方法后,线程将会一致处于阻塞状态
    #什么时候解开？释放锁定或者时间到了
    rlock.acquire()
    global num2
    num2 +=1
    time.sleep(1)
    print(num2)
    #释放锁定
    rlock.release()
for i in range(0,10):
    t = threading.Thread(group=None,name=None,target=is_lock,args=(i,))
    t.start()
