# 名片管理系统

# 名片信息

def menu():
    print("*" * 30)
    print(
    """欢迎来到名片信息管理系统！
    1.新增名片
    2.显示全部
    3.查询名片
    4.退出系统""")
    print("*" * 30)

menu()
# 名片存放

list1 = [
    {"name": "jack", "age": 18, "gender": "男"},
    {"name": "mia", "age": 23, "gender": "女"},
    {"name": "rose", "age": 19, "gender": "女"}
]
# 新增名片
def add_cards(name, age, gender):
    dict1 = dict()
    dict1["name"] = name
    dict1["age"] = age
    dict1["gender"] = gender
    list1.append(dict1)
    return True


# 查看名片
def show_cards():
    for e in list1:
        print(e)

# 查询名片
def query_cards(queryName):
    for e in list1:
        for value in e.values():
            if value == queryName:
                return e
    return False
# 退出系统
def quit_system():
    print("感谢你使用本系统！")


# 删除名片信息

def del_cards(value):
    list1.remove(value)
    return True

# 修改名片信息

def update_cards(value, dict2):
    value.update(dict2)
    return value


while True:
    op = input("请输入你的操作数：")
    if op == "1":
        name = input("请输入你的名字:")
        age = input("请输入你的年龄:")
        gender = input("请输入你的性别:")
        result = add_cards(name, age, gender)
        if result:
            print("%s名片新增成功" % name)
        else:
            print("%s名片新增失败" % name)
    elif op == "2":
        show_cards()
    elif op == "3":
        queryName = input("请输入需要查询的信息：")
        result = query_cards(queryName)
        if result:
            print(result)
            op1 = input("选择1修改这个名片，选择2删除这个名片！")
            if op1 == "1":
                name = input("请输修改之后的名字:")
                age = input("请输入修改之后的年龄:")
                gender = input("请输入修改之后的性别:")
                dic1 = {"name": name, "age": age, "gender": gender}
                print(update_cards(result, dic1))

            elif op1 == "2":
                result1 = del_cards(result)
                if result1:
                    print("删除名片信息成功！")
                else:
                    print("删除名片信息失败！")
            else:
                print("你的选择有误！")
        else:
            print("暂无信息！")
    elif op == "0":
        quit_system()
        break
    else:
        print("请重试!")
