# 客户端界面开发

import wx  # 界面类库

from socket import *  # 套接字
import threading  # 线程类库

class Client(wx.Frame):

    # 初始化函数
    def __init__(self):
        # 实例化属性(名字，是否连接，套接字)
        self.name = "Detail"
        self.isConnected = False
        self.client_socket = None
        # 调用父类初始化方法
        wx.Frame.__init__(self,None,title=self.name+"客户端连接", size=(480,700), pos=(1000, 80))

        # 创建面板
        self.pl = wx.Panel(self, size=(100,100), pos=(500, 80))
        # 按钮
        # 加入聊天室
        self.conn_btn = wx.Button(self.pl, label="加入聊天室", size=(160, 60), pos=(40, 30))
        # 离开聊天室
        self.disconn_btn = wx.Button(self.pl, label="离开聊天室", size=(160, 60), pos=(260, 30))
        # 清空信息
        self.clear_btn = wx.Button(self.pl, label="清空信息", size=(160, 60), pos=(40, 580))
        # 发送信息
        self.send_btn = wx.Button(self.pl, label="发送信息", size=(160, 60), pos=(260, 580))

        # 文本框(TE_READONLY:只读，wx.TE_MULTILINE：现实多行)
        self.chat_text = wx.TextCtrl(self.pl, size=(405, 340), pos=(30, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)   # 聊天文本框
        self.input_text = wx.TextCtrl(self.pl, size=(405, 100), pos=(30, 465), style=wx.TE_MULTILINE)  # 发送信息文本框


        # 按钮事件绑定
        self.Bind(wx.EVT_BUTTON, self.click_conn, self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.click_disconn, self.disconn_btn)
        self.Bind(wx.EVT_BUTTON, self.click_clear, self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.click_send, self.send_btn)

    # 点击加入聊天室按钮触发函数
    def click_conn(self, event):
        print("conn")
        # 连接客户端
        if self.isConnected == False:
            self.isConnected = True
            self.client_socket = socket()
            # 连接客户端
            self.client_socket.connect(("127.0.0.1", 8899))
            # 客户端发送消息给服务器
            self.client_socket.send(self.name.encode("utf8"))
            # 客户端接收其他客户端信息(如果直接在程序中接收，客户端会一直等待信息直接卡死，还是使用线程的方式)
            receive_thread = threading.Thread(target=self.receive_text_fun)  # 创建线程
            receive_thread.daemon = True  # 设置为守护线程
            receive_thread.start()  # 启动线程

    # 接收信息线程方法
    def receive_text_fun(self):
        try:
            if self.isConnected:
                # 客户端接收到服务器的信息
                recv_text = self.client_socket.recv(1024).decode("utf8")
                # 将信息放到聊天文本框内
            self.chat_text.AppendText(recv_text + "\n")
        except Exception as e:
            print(e)


    # 点击离开聊天室按钮触发函数
    def click_disconn(self, event):
        print("disconn")
        # 给客户端发送断开提醒
        self.client_socket.send("我要断开连接了，服务器！".encode("utf8"))
        self.isConnected = False
    # 点击清空信息按钮触发函数
    def click_clear(self, event):
        print("clear")
        self.input_text.Clear()  # 清空发送

    # 点击发送信息按钮触发函数
    def click_send(self, event):
        print("send")
        # 只有是连接状态才可以发送信息
        if self.isConnected:
            text = self.input_text.GetValue()  # 取出发送内容
            if text != "":
                self.client_socket.send(text.encode("utf8"))
                self.input_text.Clear()  # 清空发送内容





# 程序入口
if __name__  == "__main__":
    # 创建应用程序
    app = wx.App()
    # 创建窗口对象
    client = Client()
    # 显示窗口
    client.Show()
    # 一直显示
    app.MainLoop()