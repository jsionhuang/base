from multiprocessing import Process,Lock


def f(l,i):
    l.acquire()
    print('hello,handsome',i)
    l.release()

def f2(i):
    print('hello,handsome2',i)


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):#加锁，防止一行为打印完，就开始打印下一行
        Process(target=f,args=(lock,i)).start()
