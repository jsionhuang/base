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

#使用类装饰器
class Singleton(object):
    def __init__(self,_cls):
        self._cls = _cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]
@Singleton
class Cls2(object):
    def __init__(self):
        pass