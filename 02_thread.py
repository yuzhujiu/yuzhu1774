"""
带有参数的线程
"""
from threading import Thread
from time import sleep

# 带有参数的线程函数
def func(sec,name):
    print("含有参数的线程来喽")
    sleep(sec)
    print("%s 线程执行完毕"%name)

# 循环创建线程
for i in range(5):
    t = Thread(target=func,
               args=(2,),
               kwargs={"name":'T-%d'%i},
               daemon=True # 分支线程随主线程结束
               )
    t.start()