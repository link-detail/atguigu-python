# 服务端界面开发
import wx
import threading
from socket import *
from concurrent.futures import ThreadPoolExecutor  # 线程池执行方法

class Server(wx.Frame):

    # 初始化函数
    def __init__(self):
        # 实例属性
        self.isOn = False  # 服务器的启动状态
        # 创建socket对象
        self.server_socket = socket()
        # 班定ip地址和端口好
        self.server_socket.bind(("127.0.0.1", 8899))
        # 监听
        self.server_socket.listen(5)
        # 存放客户端
        self.client_thread_dict = {}
        # 线程池
        self.pool = ThreadPoolExecutor(max_workers=10)  # 线程池中最多有10个线程


        # 调用父类初始化方法
        wx.Frame.__init__(self,None, title="多人聊天室", size=(480, 700), pos=(500, 80))
        # 面板
        self.pl = wx.Panel(self, size=(100,100), pos=(500, 80))
        # 按钮（启动服务器，保存聊天记录）
        self.start_server = wx.Button(self.pl, label="启动服务器", size=(160, 60), pos=(40, 30))
        self.save_text = wx.Button(self.pl, label="保存聊天记录", size=(160, 60), pos=(260, 30))

        # 文本框
        self.chat_text = wx.TextCtrl(self.pl, size=(405, 420), pos=(30, 140), style=wx.TE_READONLY | wx.TE_MULTILINE)  # 聊天记录文本框
        # 按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.click_start_server, self.start_server)
        self.Bind(wx.EVT_BUTTON, self.click_save_text, self.save_text)

    # 点击启动服务器触发的函数
    def click_start_server(self, event):
        print("start_serve")
        # 没有启动时才能启动
        if self.isOn == False:
            self.isOn = True
            # self.server_socket.accept()  # 接收客户端请求 (这样会卡死的，如果没有客户端请求，会一直在等待，使用线程的话，线程和程序是并行的，互不干扰)
            main_thread = threading.Thread(target=self.main_thread_fun)  # 创建一个线程
            main_thread.daemon = True  # 设置为守护线程
            main_thread.start()  # 启动线程

    # 线程执行启动客户端操作
    def main_thread_fun(self):
        # 如果服务器是开启的，就一直保持客户端连接状态
        while self.isOn:
            client_socket, addr = self.server_socket.accept()
            print(addr)
            # 此时是新创建的套接字和客户端进行通信(不是之前的那个)
            client_name = client_socket.recv(1024).decode("utf8")
            print(client_name)
            # 创建线程进行操作
            client_thread = ClientThread(client_socket, client_name, self)
            # 保存客户端
            self.client_thread_dict[client_name] = client_thread
            self.pool.submit(client_thread.run)  # 将线程提交到线程池中
            # 通知所有客户端
            self.send("【服务器通知】欢迎%s进入聊天室!" % client_name)





    # 服务器群发信息
    def send(self, text):
        for client in self.client_thread_dict.values():
            if client.isOn:
                client.client_socket.send(text.encode("utf8"))




    # 点击保存聊天信息触发的函数
    def click_save_text(self, event):
        print("save_text")
        # 获取聊天记录中的内容
        record = self.chat_text.GetValue()
        with open("record.log", mode="a+", encoding="utf8") as file:
            file.write(record)



    # 线程类
class ClientThread(threading.Thread):
    # 初始化函数
    def __init__(self, thr_socket, name, thr_server):
        threading.Thread.__init__(self)
        self.client_socket = thr_socket
        self.client_name = name
        self.server = thr_server
        self.isOn = True
    # 重写run方法
    def run(self):
        while self.isOn:
            text = self.client_socket.recv(1024).docode("utf8")
            print(text)
            if text == "断开连接":
                self.isOn = False
                self.server.send('【服务器通知】%s离开了聊天室' % self.client_name)
            else:
                self.server.send("【%s】%s" % self.client_name, text)
        # 关闭套接字
        self.client_socket.close()





# 程序入口
if __name__ == "__main__":
    # 创建应用程序
    app = wx.App()
    # 创建窗口
    server = Server()
    # 显示窗口
    server.Show()
    # 一直显示
    app.MainLoop()