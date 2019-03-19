import threading,queue,time



exit_flag = 0
thread_list = ['Thread01','Thread02','Thread03','Thread04']
name_list = ['one','two','three','four']
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_id = 1


def process_data(thread_name,q):
    while not exit_flag:
        queue_lock.acquire()
        print(thread_name,'get Lock')
        if not work_queue.empty():
            data = q.get()
            #print('GET Queue',data)
            queue_lock.release()
            print(thread_name,'OUT Lock')
            #print(thread_name,data)
        else:
            queue_lock.release()
        time.sleep(1)

class MyThread(threading.Thread):
    def __init__(self,thread_id,name,q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q
    def run(self):
        print('START' + self.name)
        process_data(self.name,self.q)
        print('END' + self.name)


if __name__ == '__main__':
    for name in thread_list:
        mythread = MyThread(thread_id,name,work_queue)
        mythread.start()
        threads.append(mythread)
        thread_id += 1
    queue_lock.acquire()
    for word in name_list:
        work_queue.put(word)
    print('work_queue is okay',work_queue)
    queue_lock.release()

    while not work_queue.empty():
        pass

    exit_flag = 1

    for t in threads:
        t.join()
    print('exit main thread')