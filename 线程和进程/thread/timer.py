#Timer时Thread的派生类，在指定事件后调用一个方法
#interva指定的时间 function要执行的方法 args方法和参数

import threading

def test():
    print('hello timer')

#达成功能5秒后执行
timer = threading.Timer(interval=5,function=test)
timer.start()
