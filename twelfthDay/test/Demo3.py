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
        print(list1)
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