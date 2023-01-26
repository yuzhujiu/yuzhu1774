"""
线程 event方法
"""
from threading import Thread,Event
from time import sleep

msg = None # 通信变量
e = Event() # event 对象

def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set() # 结束19行阻塞
    sleep(5) # 继续做地下工作


t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
e.wait() # 阻塞等待
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他...无情啊哥哥....")


