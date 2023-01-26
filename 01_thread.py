"""
线程基础示例
"""
import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放：男儿当自强")
    global a
    print("a =",a)
    a = 10000

# 实例化线程对象
thread = threading.Thread(target=music)

# 启动线程 执行music
thread.start()

# 主线程来啦
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：月亮之上")

thread.join() # 阻塞等待确保分之线程结束
print("a :",a) # 10000



