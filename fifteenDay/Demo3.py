# 抽奖器

import wx

import random


class MyFrame(wx.Frame):

    prizeList = ["手机", "手表", "自行车", "电脑", "耳机"]

    def __init__(self):

        # 初始化窗口
        wx.Frame.__init__(self, None, title="抽奖器", size=(600, 750), pos=(500, 65))
        # 创建面板
        self.pl = wx.Panel(self, size=(450, 520), pos=(68, 100))
        # 设置背景颜色
        self.SetBackgroundColour((200, 255, 0))
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl, label=random.choice(self.prizeList), pos=(220, 100), style=wx.TE_CENTER)
        # 设置字体的形态(大小，字体包，字体风格，加粗)
        font = wx.Font(50, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_MAX, wx.FONTWEIGHT_BOLD)
        # 文本设置字体格式
        self.staticText.SetFont(font)
        # 按钮
        self.btn1 = wx.Button(self.pl, label="开始抽奖", pos=(150, 400))
        self.btn2 = wx.Button(self.pl, label="结束抽奖", pos=(400, 400))
        # 开始按钮绑定事件 事件类型，点击事件触发的方法，方法内传入参数
        self.Bind(wx.EVT_BUTTON, self.start, self.btn1)
        # 结束按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.stop, self.btn2)

    # 开始按钮绑定事件
    def start(self, event):
        # 建立一个定时器
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_prize, self.timer)
        self.timer.Start(10)  # 每隔10毫秒更新礼物

    # 结束按钮绑定事件
    def stop(self, event):
        self.timer.Stop()  # 停止计时器


    def update_prize(self, event):
        # 修改标签内容
        self.staticText.SetLabelText(random.choice(self.prizeList))


if __name__ == "__main__":  # python程序主入口
    # 创建应用程序对象
    app = wx.App()

    # 实例化窗口对象
    myF = MyFrame()
    myF.Show()  # 显示窗口

    # 一直显示窗口
    app.MainLoop()