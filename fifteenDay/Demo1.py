# 创建一个窗口
import wx

# 按钮绑定时间方法
def onClick(event):
    print("测试结束！")

# 创建一个应用程序对象

app = wx.App()

# 新建一个窗口 size:宽 高   pos:相较于原点（x坐标，y坐标）
frm = wx.Frame(None, title="mia学习系统", size=(600, 750), pos=(500, 65))

# 显示窗口

frm.Show()

# 新建一个面板(面板显示在窗口上)

pl = wx.Panel(frm, size=(450, 520), pos=(68, 100))

# 显示面板

pl.Show()

# 新建静态文本
staticText = wx.StaticText(pl, label="欢迎使用mia学习系统！", pos=(150, 100))
# 显示文本
staticText.Show()

# 新增一个点击按钮
btn = wx.Button(pl, label="测试按钮", pos=(190, 400))
# 显示按钮
btn.Show()

# 按钮绑定事件（参数：事件类型，触发事件进行的操作，操作按钮）
app.Bind(wx.EVT_BUTTON, onClick, btn)

# 陷入主循环(让其显示页面一直显示)

app.MainLoop()





















