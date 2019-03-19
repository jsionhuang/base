'''
适用于高并发
本质单线程
协程配合进程 多CPU运行
'''
# 使用yeild模拟多协程，模拟多并发
import time
import queue


#自动切换
import gevent

def foo():
    print("Running in foo,foo开始>>>1")
    gevent.sleep(2)
    print('Explicit context switch to foo again  foo完成>>>6')

def bar():
    print('Explicit精确的 context 内容 to bar   bar开始>>>2')
    gevent.sleep(1)
    print("Imlicit context sitch back to bar  bar结束>>>5")

def func3():
    print('running func3  func3开始>>>3')
    gevent.sleep(0)
    print('running func3 again  func3结束>>>4')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(func3),
])