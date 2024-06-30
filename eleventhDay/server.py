# socket服务端

import socket

socket1 = socket.socket()  # 建立一个客户端

socket1.bind(("0.0.0.0", 9876))  # 绑定ip地址

socket1.listen(5)  # 设置最大连接数

sock, addr = socket1.accept()  # 等待客户端连接(一个是客户端套接字和客户端的地址)

print(sock)
print(addr)

while True:
    accept_data = sock.recv(1024)  # 接收信息
    print("服务端收到消息-->%s" % accept_data.decode("utf8"))
    send_data = "服务端收到！"
    sock.send(send_data.encode("utf8"))  # 发送信息




