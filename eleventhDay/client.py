# 客户端

import socket

socket1 = socket.socket()  # 建立连接

socket1.connect(("127.0.0.1", 9876))  # 连接服务端

print(socket1)

while True:
    send_data = input("请输入需要发送的消息:")
    socket1.send(send_data.encode("utf8"))  # 设置编码格式
    accept_data = socket1.recv(1024)  # 设置最大接收字节数
    print("接收到服务端的回信%s" % accept_data.decode("utf8"))
