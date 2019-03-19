'''
一个父进程分为两个子进程，一个读，一个写
'''

from multiprocessing import Process,Queue
import os,random,time

#写数据进程执行的代码
def write(q):
    print('{}process to write'.format(os.getpid()))
    for val in ['A','B','C']:
        print('将{}放入消息队列'.format(val))
        q.put(val)
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
if __name__ == '__main__':
    #父进程创建Quenen并传给子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动写入 子进程
    print('启动写入的子进程')
    pw.start()
    #起订读取子进程
    pr.start()
    #等到 写入子进程结束
    pw.join()
    pr.terminate()#pr子进程是死循环，只能强制结束