import time
import threading


#使用函数装饰器
def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner
@singleton
class Cls(object):
    def __init__(self):
        pass

c1 = Cls()
c2 = Cls()
print(c1 == c2)

#一般的单例模式
class Singleton(object):
    def __init__(self):
        time.sleep(1)#模拟io操作，多线程会出现错误
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

import threading



def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


def Singleton(cls):
    instances = {}
    @synchronized
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


def worker():
    single_test = test()
    print ("id----> %s" % id(single_test))


@Singleton
class test():
    a = 1

if __name__ == "__main__":
    task_list = []
    for one in range(30):
        t = threading.Thread(target=worker)
        task_list.append(t)

    for one in task_list:
        one.start()

    for one in task_list:
        one.join()
