# 名片管理系统
# 信息：姓名 电话 QQ 邮箱

# 系统目录
def menu():
    print("*" * 30)
    print(
    """[欢迎来到名片信息管理系统!]
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统""")
    print("*" * 30)
menu()

# 退出系统
def quit():
    print("感谢你使用本系统!")

# 新增名片

list1 = [{"name": "tom", "phone": "123", "qq": "123", "email": "123"},
         {"name": "mia", "phone": "456", "qq": "456", "email": "456"},
         {"name": "jack", "phone": "789", "qq": "789", "email": "789"}]  # 收集所有名片

def add_infos(name, phone, qq, email):
    dict1 = {}
    dict1["name"] = name
    dict1["phone"] = phone
    dict1["qq"] = qq
    dict1["email"] = email
    list1.append(dict1)
    return True

# 展示名片

def show_infos():
    for e in list1:
        print(e)

# 查询名片

def query_infos(query):
    for i in list1:
        for value in i.values():
            if query == value:
                return i

    return False

while True:
    op = int(input("请输入你的操作序号:"))
    if op == 1:
        name = input("请输入你的姓名:")
        phone = input("请输入你的电话:")
        qq = input("请输入你的qq:")
        email = input("请输入你的邮箱:")
        result = add_infos(name, phone, qq, email)
        if result:
            print("新增%s的名片成功！" % name)
        else:
            print("请重试！")
    elif op == 2:
        show_infos()
    elif op == 3:
        query = input("请输入需要查询的信息名片信息:")
        result = query_infos(query)
        if result:
            print(result)
        else:
            print("没有找到相关信息！")
    elif op == 0:
        quit()
        break
    else:
        print("请重试!")


