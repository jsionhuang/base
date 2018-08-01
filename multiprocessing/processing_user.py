from  multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print("Run child proccess {0} ({1})".format(name,os.getpid()))

if __name__ == '__main__':
    print('Parent proccess is {}'.format(os.getpid()))
    p = Process(target=run_proc,args=('test',))
    print('Child Process will strat')
    p.start()
    p.join()
    print('Child is end')

