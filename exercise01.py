"""
现在有500张票，存在一个列表中 ["T1",...."T500"]，
10个窗口同时卖这500张票 W1-W10

使用10个线程模拟这10个窗口，同时卖票，
直到所有的票都卖出为止，
每出一张票 需要0.1秒，
打印表示即可print("W1----T250")
"""
from threading import Thread
from time import sleep

# 生成车票
tickets = ["T%d"%i for i in range(1,501)]

# 每个线程都买票
def sell(w):
    while tickets:
        # 取出的就是票
        print("%s --- %s"%(w,tickets.pop(0)))
        sleep(0.1)

# 改造上面的函数，只要先sleep 后 打印，保证无错误
# 每张票sleep 0.1



jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    jobs.append(t) # 存储线程对象
    t.start()

# 所有线程都执行结束
for i in jobs:
    i.join()
print("票已售罄")






