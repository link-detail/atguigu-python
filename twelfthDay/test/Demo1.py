# 日记本

# 封面

def menu():
    print("*" * 30)
    print("""欢迎来到日记管理系统！
    1.写日记
    2.查日记
    C.退出系统""")

# 退出系统

def quit():
    print("感谢你使用本系统！")

# 写日记

def write_diary():
    try:
        day = input("请输入你的日期:")
        context = input("请输入你需要记录的内容:")
        f1 = open("diary.md", mode="a", encoding="utf8")  # 打开文件
        f1.write("pyrjb"+"\n")
        f1.write(day+"\n")  # 写入内容
        f1.write(context+"\n")
        f1.close()  # 关闭文件
        return True
    except Exception as e:
        print("写入内容失败！", e)


# 查看日记
def show_diary(day = "-1"):
    f1 = open("diary.md", mode="r", encoding="utf8")
    context = f1.read()
    f1.close()
    if day != "-1":
        list1 = context.split("pyrjb\n")
        for e in list1:
            if day == e[:10]:
                print(e)
                return True
        print("未查询到相关内容！")
        return False

    else:
        context = context.replace("pyrjb\n", "")
        print(context)
        return True


while True:
    menu()
    op = input("请输入你的选择：")
    if op == "1":
        result = write_diary()
        if result:
            print("写入成功！")
        else:
            print("写入失败")
    elif op == "2":
        day = input("请输入你的查询日期：")
        result = show_diary(day)
        if result:
            print("加载成功！")
        else:
            print("加载失败！")
    elif op == "C":
        quit()
        break
    else:
        print("请重试!")
