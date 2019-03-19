import threading
import time
#condition 它包含rlock的锁定池还包含一个等待池
product = None
con  = threading.Condition()

def produce():
    global product
#进入阻塞状态，和通知
    if con.acquire():
        while True:
            if product is None:
                print('produce')
                product = 'somethong'
                #通知消费者商品已经生产好了
                #唤醒消费者的进程
                con.notify()#从等待池挑选一个线程并通知，收到的线程会自动调用acquire尝试获得锁定
            #等待通知
            con.wait()#进入condition的等待池
            time.sleep(2)
def consum():
    global product
    if con.acquire():
        while True:
            if product is not None:
                print("consum")
                product = None

                #通知生产之商品没了，唤醒生产的进程
                con.notify()
            #等待通知
            con.wait()
            time.sleep(2)

produce_thread = threading.Thread(group=None,name=None,target=produce)
consum_thread = threading.Thread(target=consum)
produce_thread.start()
consum_thread.start()