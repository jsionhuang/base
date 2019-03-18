import threading
import psycopg2
class ConnSingleton(object):
    _instance_lock = threading.Lock()

    def __init__(self,dataname,username,password,hosts):
        self.dataname = dataname
        self.username = username
        self.password = password
        self.hosts = hosts

    def __new__(cls, *args, **kwargs):
        if not hasattr(ConnSingleton, "_instance"):
            with ConnSingleton._instance_lock:
                if not hasattr(ConnSingleton, "_instance"):
                    ConnSingleton._instance = object.__new__(cls)
        return ConnSingleton._instance

    def get_conn(self):
        conn = psycopg2.connect(database=self.dataname, user=self.username, password=self.password, host=self.hosts)
        return conn

obj1 = ConnSingleton('cms','postgres','root','localhost')
obj2 = ConnSingleton('cms','postgres','root','localhost')
print(obj1.get_conn(),obj2.get_conn())

def task(arg):
    obj = ConnSingleton('cms','postgres','root','localhost')
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()