# 客户端
import socket

# 创建socket对象
sk = socket.socket()

# 连接服务器
sk.connect(("127.0.0.1", 8996))

# 发送数据到服务器

while True:
    send_date = input("请输入你需要发送的数据--》")
    # 发送服务器
    sk.send(send_date.encode("utf8"))  # 设置编码格式
    # 接收服务器的返回
    accept_data = sk.recv(1024)  # 设置最大接收文件字节
    # 打印接收结果
    print("接收到服务器的响应：%s" % accept_data.decode("utf8"))   # 解码