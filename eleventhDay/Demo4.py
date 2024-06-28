# socket 库

# 服务端
import socket

# 创建一个socket客户端
sk = socket.socket()

# 绑定ip和端口号
sk.bind(("0.0.0.0", 8996))

# 设置监听（就是客户端的最大连接数）
sk.listen(5)

# 等待客户端连接
conn, addr = sk.accept()

print(conn)
print(addr)


while True:
    accept_data = conn.recv(1024)
    print("收到客户端发送的消息:%s" % accept_data.decode("utf8"))
    # 响应信息给客户端
    send_date = "服务器收到！"
    conn.send(send_date.encode("utf8"))
