#local时一个小写字符开头的类，用于管理thread-local(线程局部的数据)。
#对于同一个local，线程无法访问其他线程设置的属性
import threading

local = threading.local()
local.tname = 'main'

def test():
    local.tname = 'notmain'
    print(local.tname)

t1 = threading.Thread(target=test)
t1.start()
t1.join()
#对设置了local的字符，在线程中是无法改变的
print(local.tname)
