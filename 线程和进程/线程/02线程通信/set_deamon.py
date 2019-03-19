import threading
import time

def action(arg):
    time.sleep(1)
    print('the threading name is :'+threading.currentThread().getName())
    print('the arg is :'+str(arg))
    time.sleep(1)

for i in range(0,4):
    #默认值是前台线程，主线程执行过程中，前台线程也在执行，等带前台线程执行后，程序停止
    t = threading.Thread(group=None,name=None,target=action,args=(i,))
    #默认值就是false 也就是前台线程
    t.setDaemon(False)
    #t.start()
print('前台线程执行结束')

for i in range(0,4):
#接下来弄一个后台线程
    t = threading.Thread(group=None,name=None,target=action,args=(i,));
#后台线程就是主线程执行过程中，后台线程也执行，当主线程执行结束时，不管后台线程是否执行成功，主线程都结束
    t.setDaemon(True)
    t.start()
print('后台线程执行结束')

