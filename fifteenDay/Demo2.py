# 窗口类

import wx

# 创建应用程序对象

app = wx.App()

class MyFrame(wx.Frame):

    def __init__(self):

        # 初始化窗口
        wx.Frame.__init__(self, None, title="mia学习系统!", size=(600, 750), pos=(500, 65))
        # 创建面板
        self.pl = wx.Panel(self, size=(450, 520), pos=(68, 100))
        # 显示面板
        self.pl.Show()
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl, label="欢迎使用mia学习系统", pos=(220, 100))
        # 显示文本
        self.staticText.Show()
        # 按钮
        self.btn = wx.Button(self.pl, label="测试按钮", pos=(250, 400))
        # 显示按钮
        self.btn.Show()
        # 按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.onClick, self.btn)

        # 按钮绑定事件

    def onClick(self, event):
        print("测试结束！")

# 实例化对象
myF = MyFrame()
myF.Show()  # 显示窗口


# 一直显示窗口
app.MainLoop()