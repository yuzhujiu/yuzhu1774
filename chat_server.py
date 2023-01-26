"""
Name : Levi
Email : lvze@tedu.cn
Date : 2021-12-14
Env : Python3.6

群聊聊天室服务端训练：udp网络 多进程编程  函数结构
"""
from multiprocessing import Process
from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息 ： {name: address}
user = {}


# 处理进入
def login(sock, name, addr):
    # 判断
    if name in user or "管" in name:
        sock.sendto(b"FAIL", addr)
    else:
        sock.sendto(b"OK", addr)
        msg = "欢迎 %s 加入群聊" % name
        for key, val in user.items():
            sock.sendto(msg.encode(), val)
        user[name] = addr  # 添加用户信息
        # print(user)  # 测试


# 处理聊天
def chat(sock, name, content):
    pass
    msg = "%s : %s" % (name, content)
    # 转发给其他人
    for key, val in user.items():
        if key == name:
            continue
        sock.sendto(msg.encode(), val)


# 处理退出
def quit(sock, name):
    del user[name]  # 删除用户
    # 告知其他人
    msg = "%s 退出群聊" % name
    for key, val in user.items():
        sock.sendto(msg.encode(), val)

# 子进程函数，负责接收请求
def handle(sock):
    # 总分结构 ： 总体接收请求，分情况讨论
    while True:
        request, addr = sock.recvfrom(1024)
        # 请求简单解析
        tmp = request.decode().split(' ', 2)
        if tmp[0] == "LOGIN":
            login(sock, tmp[1], addr)  # tmp --> [LOGIN,name]
        elif tmp[0] == "CHAT":
            chat(sock, tmp[1], tmp[2])  # [CHAT,name,content]
        elif tmp[0] == "QUIT":
            quit(sock, tmp[1])  # [QUIT,name]


# 服务的入口
def main():
    # udp套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    # 创建子进程
    p = Process(target=handle,args=(sock,),daemon=True)
    p.start()
    # 发送管理员消息
    while True:
        content = input("管理员消息:")
        if content == "quit":
            break  # 解散聊天室
        msg = "CHAT 管理员消息 " + content
        sock.sendto(msg.encode(), ADDR)
    sock.close()



if __name__ == '__main__':
    main()
