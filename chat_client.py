"""
聊天室客户端
"""
from socket import *
from multiprocessing import Process

# 访问服务端的地址
ADDR = ("121.5.90.43", 8888)


# 请求进入
def login(sock):
    while True:
        name = input("请输入昵称:")
        if ' ' in name or len(name) < 3:
            print("名字太短啦！")
            continue
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(1024)
        if result == b'OK':
            print("您已进入聊天室")
            return name
        print("您的昵称太受欢迎了，换一个吧。")


# 子进程函数
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 1024)
        print("\n" + data.decode() + "\n发言:", end="")


# 请求聊天
def chat(sock, name):
    # 创建子进程接收
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    while True:
        content = input("发言:")
        if not content or content == 'quit':
            break  # 发动结束
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), ADDR)


# 请求退出
def quit(sock, name):
    msg = "QUIT " + name
    sock.sendto(msg.encode(), ADDR)
    print("您已退出群聊")


# 入口函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    name = login(sock)  # 登录的用户名
    chat(sock, name)
    quit(sock, name)
    sock.close()


if __name__ == '__main__':
    main()
