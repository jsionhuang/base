import threading
import time

product = 0
condition = threading.Condition()

class Product(threading.Thread):
    def run(self):
        global product
        while True:
            if condition.acquire():
                if product < 10:
                    product += 1;
                    print("Producer(%s):deliver one, now products:%s" %(self.name, product))
                #唤醒另外一个等待池中的进程
                condition.notify()
                #释放进程
                condition.release()
            else:
                # 如果商品达到最大值
                print("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, product))
                #自动释放锁定,等待唤醒
                condition.wait()
class Consum(threading.Thread):
    def run(self):
        global product
        while True:
            if condition.acquire():
                if product > 1:
                    product -=1
                    print("Consumer(%s):consume one, now products:%s" %(self.name, product))
                    #通知可以生产了
                    condition.notify()
                    #释放进程
                    condition.release()
                else:
                    #只有1见商品，不能消费了
                    print("Consumer(%s):only 1, stop consume, products:%s" %(self.name, product))
                    #消费者等待
                    condition.wait()
                time.sleep(2)
if __name__ == '__main__':
    for p in range(0,2):
        p = Product()
        p.start()
    for c in range(0,3):
        c = Consum()
        c.start()






