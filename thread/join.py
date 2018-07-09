import time
import threading

class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg = arg
    def run(self):
        time.sleep(1)
        print('the thread name is'+threading.currentThread().getName())
        print('the arg is'+str(self.arg))
        time.sleep(1)

thread_list = []
for i in range(0,4):
    t = MyThread(i)
    t.setDaemon(True)
    thread_list.append(t)
#for t in thread_list:
    #t.start()
#for t in thread_list:
    #join的作用就是及时设置了setDaemon，主线程还是需要等待后台线程执行完才能结束
    #t.join()
#join的错误使用
for i in range(0,4):
    t = MyThread(i)
    t.start()
    t.join()
#这些会导致线程按照顺序执行，失去多线程的意义

