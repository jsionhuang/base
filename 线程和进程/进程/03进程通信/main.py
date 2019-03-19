'''
首先线程是数据共享，需要做的是lock
而不同进程之间是相互独立的(不共享，父进程和子进程也不)，那么他们要如何进行通信？
两个进程之间是完全独立的内存空间
Queue，和Pipe可以实现进程之间的直接通信，Manager可实现数据共享

'''
from multiprocessing import Process,Queue,Pipe,Manager
import queue,os



def run(q):
    q.put('测试')

def f(conn):
    conn.send([42,None,'hello from child1'])
    conn.send([42,None,'hello from child2'])
    print('from parent',conn.recv())
    conn.close()

def f_manager(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    q_thread = queue.Queue()#基于线程的queue，会报错
    q_process = Queue()#进程的queue
    process = Process(target=run,args=(q_process,))
    process.start()
    print(q_process.get())
    process.join()


    '''
    父进程和子进程虽然不能互相通信，但是子进程能够获取父进程的数据
    流程如下：
    子进程生成是把父进程当作一个变量拿过来，其实就是拿到queue里面的q,
    然后子进程copy一份
    然后用pickle进行序列化，再反系列化给父进程
    故子进程能够访问父进程的数据
    '''



    parent_conn,chlid_conn = Pipe()
    #开启一个进程
    process_01 = Process(target=f,args=(chlid_conn,))
    process_01.start()
    #看父进程收到的消息
    print(parent_conn.recv())
    parent_conn.send('儿子可好')
    process_01.join()


    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))

        process_list = []
        for i in range(10):
            process = Process(target=f_manager,args=(d,l))
            process.start()
            process_list.append(process)
        for res in process_list:
            res.join()
        print(d)
