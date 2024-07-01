# # 读取文件步骤
# import os
# # 打开文件
# f1 = open("hello.txt", encoding="utf8")  # 相对路径
# f1 = open("F:/pythonDev/atguigu-python/twelfthDay/hello.txt", encoding="utf8")  # 绝对路径写法
# f2 = open("../test.txt", encoding="utf8")  # ../根目录
# content = f2.read()
# print(content)
# f2.close()
# # 读取文件
# context = f1.read()
# print(context)
#
# # 关闭文件
# f1.close()


# import os
#
# path = os.getcwd()  # 获取当前文件夹绝对路径
# print(path)
# fileName = path + "/hello.txt"
# f1 = open(fileName, encoding="utf8")
# context = f1.read()
# print(context)
# f1.close()

# import os
#
# path = os.getcwd()  # 获取文件夹路径
#
# filename = path + "/hello.txt"
#
# f1 = open(filename, mode="r", encoding="utf8")  # 打开文件
#
# context = f1.read()  # 读取文件
# print(context)
#
# f1.close()  # 关闭文件


# f1 = open("hello.txt", encoding="utf8")
#
# # 指定读取几个字符(换行也是代表一个字符) 没有加就是全部读取出来
# context = f1.read(5)
# print(context)
#
# # 读取一行
# context = f1.readline()
# print(context)
#
# # 讲读取出来的内容放到一个列表中
# context = f1.readlines()
# print(context)
#
#
# f1.close()


# 写入文件
#
# f1 = open("world1.md", mode="w", encoding="utf8")
#
# f1.write("你好\n")
# f1.write("hello\n")
# f1.writelines(["你好\n", "我叫刘熬好\n"])
#
# f1.close()
#
#
# # 再次读取写入内容
#
# f2 = open("world1.md", encoding="utf8")
#
# context = f2.readlines()
# str = ""
#
# for e in context:
#     str += e
#
# print(str)





#
# # 文件追加
#
# # 打开文件
# f1 = open("hello.txt", mode="a", encoding="utf8")
#
# # 写入内容
# # context = f1.write("你好\n")
# list1 = ["hello\n", "你好\n", "萨卡尼瓦\n"]
#
# f1.writelines(list1)
#
#
# # 关闭文件
# f1.close()

# 页面

def menu():
    print("*"*30)
    print("""欢迎使用日记管理系统！
    1.写日记
    2.看日记
    C.退出系统""")
    print("*"*30)

# 退出

def quit():
    print("感谢你使用本日记管理系统！")


# 写日记
def write_txt():
    date = input("请输入你的日记日期：")
    text = input("请输入你的日记内容:")
    f = open("diray/dirays.md", mode="a", encoding="utf8")  # 打开文件
    f.write("pyrjb\n")  # 如果日记内容写的多，我们就用这个来分割每一篇日记
    f.write(date+"\n")  # 写入日期
    f.write(text+"\n")  # 写入内容
    f.close()  # 关闭文件
    return True

def show_txt(day = "-1"):
    f = open("diray/dirays.md", encoding="utf8")
    context = f.read()
    f.close()
    if day != "-1":
        list1 = context.split("pyrjb\n")
        for e in list1:
            if e[:10] == day:
                print(e)
                return True
        return False
    else:
        newContext = context.replace("pyrjb", " ")  # 替换我们的标记
        print(newContext)
        return True




while True:
    menu()
    op = input("请输入你的选择:")
    if op == "1":
       if write_txt():
           print("日记写入成功！")
       else:
           print("日记写入失败！")
    elif op == "2":
        op1 = input("请输入你的查询日期(-1表示查询所有日记):")
        if show_txt(op1):
            print("日记加载完成！")
        else:
            print("日记加载失败！")
    elif op == "C":
        quit()
        break
    else:
        print("请重试！")















