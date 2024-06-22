# # 集合
#
# s1 = set()
# print(type(s1))
# s2 = {"hello", 1, "world"}
# print(s2)
# s3 = {1, 2, 3, 4, 5}
#
# print(len(s3))
# print(max(s3))
# print(min(s3))
#
# # str -->set
# d1 = set("hello")
# print(d1)
# # list --> set
# d2 = set(["hello", "world", 1, 2, 3])
# print(d2)
# # tuple -- set
# d3 = set(("1", 2, 1, 1))
# print(d3)
# # dict --> set
# d4 = set({"name": "jack", "age": 12 })
# print(d4)


# 常用方法



# s1.add("hello")
# print(s1)
# s3 = s1.copy()
# print(s3)
# s1.pop()
# print(s1)
# s1.remove("hello")
# print(s1)
# s1.update(["jack", "rose"])
# print(s1)


# 不可变 str int bool set

# 用户登陆系统

users = {
    "rose": {"pwd": "123", "status": True},
    "jack": {"pwd": "345", "status": True},
    "mia": {"pwd": "567", "status": False}
}


for i in range(3):

    user = input("请输入你的账号-->")
    pwd = input("请输入你的密码-->")
    if user in users and pwd == users[user]["pwd"] and users[user]["status"]:
        print(user, "登陆成功!")
        break
    elif user in users and pwd == users[user]["pwd"] and not users[user]["status"]:
        print("该用户已经被封禁,请联系管理员!")
    elif user in users and pwd != users[user]["pwd"]:
        print("密码错误!")
    else:
        print("该用户未注册!")

