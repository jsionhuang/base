#thread 是线程类 有两种使用方法
#1.直接传入要运行的方法
#2.从thread类继承并覆盖run()
import threading
import time

def action(arg):
    time.sleep(1)
    print(arg)

for i in range(0,4):
    #直接传入要运行的方法
    t = threading.Thread(group=None,name=None,target=action,args=(i,))
    t.start()

#方法重写run方法
class MyThread(threading.Thread):
    def __init__(self,arg):
        #继承父类的初始化方法
        super(MyThread,self).__init__()
        self.arg = arg
    def run(self):
        time.sleep(1)
        print(self.arg)
for i in range(0,4):
    t = MyThread(i)
    t.start()