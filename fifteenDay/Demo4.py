# 计算器界面布局
import wx

class MyFrame(wx.Frame):

    w, h = 80, 80
    x, y = 10, 80

    def __init__(self):
        # 创建窗口
        wx.Frame.__init__(self, None, title="计算器", size=(440, 650), pos=(500, 65))
        # 创建面板
        self.pl = wx.Panel(self, size=(500, 400), pos=(200, 100))
        # 创建文本框
        self.entry = wx.TextCtrl(self.pl, pos=(10, 10), size=(400, 50))
        # 创建按钮(第一行)
        self.btn_clear = wx.Button(self.pl, label="C", size=(self.w,self.h), pos=(self.x, self.y))
        self.btn_div = wx.Button(self.pl, label="/", size=(self.w,self.h), pos=(self.x+100, self.y))
        self.btn_mul = wx.Button(self.pl, label="*", size=(self.w,self.h), pos=(self.x+200, self.y))
        self.btn_back = wx.Button(self.pl, label="<-", size=(self.w,self.h), pos=(self.x+300, self.y))
        # 创建按钮(第二行)
        self.btn7 = wx.Button(self.pl, label="7", size=(self.w,self.h), pos=(self.x, self.y+100))
        self.btn8 = wx.Button(self.pl, label="8", size=(self.w,self.h), pos=(self.x+100, self.y+100))
        self.btn9 = wx.Button(self.pl, label="9", size=(self.w,self.h), pos=(self.x+200, self.y+100))
        self.btn_sub = wx.Button(self.pl, label="-", size=(self.w,self.h), pos=(self.x+300, self.y+100))
        # 创建按钮(第三行)
        self.btn4 = wx.Button(self.pl, label="4", size=(self.w,self.h), pos=(self.x, self.y+200))
        self.btn5 = wx.Button(self.pl, label="5", size=(self.w,self.h), pos=(self.x+100, self.y+200))
        self.btn6 = wx.Button(self.pl, label="6", size=(self.w,self.h), pos=(self.x+200, self.y+200))
        self.btn_add = wx.Button(self.pl, label="+", size=(self.w,self.h), pos=(self.x+300, self.y+200))
        # 创建按钮(第四行)
        self.btn1 = wx.Button(self.pl, label="1", size=(self.w,self.h), pos=(self.x, self.y+300))
        self.btn2 = wx.Button(self.pl, label="2", size=(self.w,self.h), pos=(self.x+100, self.y+300))
        self.btn3 = wx.Button(self.pl, label="3", size=(self.w,self.h), pos=(self.x+200, self.y+300))
        self.btn_eq = wx.Button(self.pl, label="=", size=(self.w,(self.h*2)+20), pos=(self.x+300, self.y+300))
        # 创建按钮(第五行)
        self.btn0 = wx.Button(self.pl, label="0", size=((self.w*2)+20,self.h), pos=(self.x, self.y+400))
        self.btn_point = wx.Button(self.pl, label=".", size=(self.w,self.h), pos=(self.x+200, self.y+400))

        # 绑定按钮对应的事件
        self.Bind(wx.EVT_BUTTON, self.on_btn_clear, self.btn_clear)
        self.Bind(wx.EVT_BUTTON, self.on_btn_div, self.btn_div)
        self.Bind(wx.EVT_BUTTON, self.on_btn_mul, self.btn_mul)
        self.Bind(wx.EVT_BUTTON, self.on_btn_back, self.btn_back)
        self.Bind(wx.EVT_BUTTON, self.on_btn7, self.btn7)
        self.Bind(wx.EVT_BUTTON, self.on_btn8, self.btn8)
        self.Bind(wx.EVT_BUTTON, self.on_btn9, self.btn9)
        self.Bind(wx.EVT_BUTTON, self.on_btn_sub, self.btn_sub)
        self.Bind(wx.EVT_BUTTON, self.on_btn4, self.btn4)
        self.Bind(wx.EVT_BUTTON, self.on_btn5, self.btn5)
        self.Bind(wx.EVT_BUTTON, self.on_btn6, self.btn6)
        self.Bind(wx.EVT_BUTTON, self.on_btn_add, self.btn_add)
        self.Bind(wx.EVT_BUTTON, self.on_btn1, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.on_btn2, self.btn2)
        self.Bind(wx.EVT_BUTTON, self.on_btn3, self.btn3)
        self.Bind(wx.EVT_BUTTON, self.on_btn_eq, self.btn_eq)
        self.Bind(wx.EVT_BUTTON, self.on_btn0, self.btn0)
        self.Bind(wx.EVT_BUTTON, self.on_btn_point, self.btn_point)


    def on_btn0(self, event):
        self.entry.AppendText("0")
    def on_btn1(self, event):
        self.entry.AppendText("1")
    def on_btn2(self, event):
        self.entry.AppendText("2")
    def on_btn3(self, event):
        self.entry.AppendText("3")
    def on_btn4(self, event):
        self.entry.AppendText("4")
    def on_btn5(self, event):
        self.entry.AppendText("5")
    def on_btn6(self, event):
        self.entry.AppendText("6")
    def on_btn7(self, event):
        self.entry.AppendText("7")
    def on_btn8(self, event):
        self.entry.AppendText("8")
    def on_btn9(self, event):
        self.entry.AppendText("9")
    # 清除
    def on_btn_clear(self, event):
        self.entry.Clear()
    # 除法
    def on_btn_div(self, event):
        self.entry.AppendText("/")
    # 乘法
    def on_btn_mul(self, event):
        self.entry.AppendText("*")
    # 返回
    def on_btn_back(self, event):
        text = self.entry.GetValue()  # 获取文本内容
        self.entry.SetValue(text[:-1])  # 把文本最后一个元素去掉
    # 减法
    def on_btn_sub(self, event):
        self.entry.AppendText("-")
    # 加法
    def on_btn_add(self, event):
        self.entry.AppendText("+")
    # 等于
    def on_btn_eq(self, event):
        text = self.entry.GetValue()  # 获取输出区内容
        result = str(eval(text))  # 处理文本算式
        self.entry.SetValue(result)  # 设置输入区显示内容
    # .
    def on_btn_point(self, event):
        self.entry.AppendText(".")

if __name__ == "__main__":
    # 创建一个应用程序
    app = wx.App()
    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()
    # 一直显示
    app.MainLoop()
