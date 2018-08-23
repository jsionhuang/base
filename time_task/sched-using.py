import time
import sched
import threading
import datetime

def worker(msg,starttime):#第一个工作函数
    print('任务执行的时刻',time.strftime('%Y-%m-%d %H:%M:%S'),'传达的消息是',msg,'任务建立的时候',starttime)

print('程序启动时刻',time.strftime('%Y-%m-%d %H:%M:%S'))
s1 = sched.scheduler(time.time,time.sleep)#引入调度器
s1.enter(1,1,worker,('hello',time.strftime('%Y-%m-%d %H:%M:%S')))#建立任务1
s1.enter(3,1,worker,('world',time.strftime('%Y-%m-%d %H:%M:%S')))#建立任务2
s1.run()# run启动上面两个任务
print('准备睡眠2秒')
time.sleep(2)
print('睡眠2秒结束')

def doSth():
    print('test')
    #假如完成这件事需要一分钟
    time.sleep()
def main(h=0,m=0):
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour==h and now.minute==m:
                break
            time.sleep(20)#20秒检查一次
        doSth()

main(17,50)