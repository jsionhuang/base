#是要用进程词 大量创建子进程

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('run proccess is ',os.getpid())
    statt = time.time()
    time.sleep(random.random()*3)#sleep用来暂停线程执行
    end = time.time()
    print('task{0},run{1}秒'.format(name,(end-statt)))
if __name__ == '__main__':
    print('parent process is{}'.format(os.getpid()))
    p = Pool(4)#pool的默认大小是cpu的核数
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done....')
    p.close()#close之后就不能添加新的进程
    p.join()#会等待所有子程序执行完毕
    print('all subprocess done')