# # 集合(无序不可重复的)
# s1 = set()
#
# print(s1, type(s1))
# s = {1, "hello", 2, 1, 3}
#
# print(s)
#
# # 类型转换
#
# s2 = set("123124")  # str --> set
# print(s2)
#
# s3 = set(["1", 1, "hello"])  # list --> set
# print(s3)
#
# s4 = set((1, "2", "hello"))   # tuple -->set
# print(s4)
#
# s5 = set({"name":"jack", 1:"a"})  # dict --> set  # 取出的是key的值
# print(s5)
#
#
# s6 = {1, 2, 3}
# print(1 in s6)  # 是否包含某一个元素
#
# print(1 not in s6)  # 是否不包含某个元素
#
#
# print(len(s6))  # 长度
# print(max(s6))  # 最大值
# print(min(s6))  # 最小值
#
# del s6  # 删除集合
#
# print(s6)


# 集合遍历

# s = {1, "hello", 2, "world"}
# for e in s:
#     print(e)
#
#
# for i, e in enumerate(s):
#     print(i, e)

# 常用方法



# s1.pop()  # 删除一个元素
# print(s1)
#
# s3 = s1.copy()  # 拷贝一个集合
# print(s3)
#
# s1.update({4, 5, 6})  # 更新集合中的元素：后面跟着的是一个集合类型
# print(s1)
#
# s1.add("hello")  # 添加一个元素
# print(s1)
#
# s1.remove("hello")  # 删除一个元素
# print(s1)
#
# # s1.clear()  # 清空一个元素
# print(s1)
#
# print("不同的是", s2.difference(s1))  # s2相比于s1不同的元素


# 交集并集

# s1 = {1, 2, 3, 4}
# s2 = {4, 5, 6}
#
# print(s1 & s2)  # 交集
#
# print(s1 | s2)  # 并集

# 列表去重

# l1 = [80, 90, 70, 60, 80, 90]
#
# s1 = set(l1)
#
# print(s1)

# 统计每一个分数段的人数


# d1 = {}  # 字典去储存
#
# for e in s1:
#     t = l1.user(e)
#     print("%d分的有%d个人" %(e, t))
#     d1[e] = t
#
# print(d1)
#
# for k, v in d1.items():
#     print("%d分的有%d个人" %(k, v))



# 可变与不可变

#
# l1 = [1, 3, 5, 7]
#
# print(l1)
#
# l1[0] = 2
#
# print(l1)
#
# d1 = {"name": "jack", "age": 12}
# print(d1)
#
# d1["name"] = "roise"
#
# s1 = {1, 2, 3}
# print(s1)
#
# tup1 = (1, 2, 4)
# print(tup1.index(2))

# 用户登陆系统1

# 用户输入账号，密码后，根据用户是否已经注册，用户是否在黑名单中，提示用户是否登陆成功

users = {
    "jack": {"name": "jack", "pd": "123", "status": True},
    "rose": {"name": "rose", "pd": "456", "status": True},
    "mia": {"name": "mia", "pd": "789", "status": False}

}


for i in range(3):
    user = input("请输入你的用户名-->")
    pwd = input("请输入你的密码-->")
    if user in users and users[user]["pd"] == pwd and users[user]["status"]:
        print(user, "登陆成功")
    elif user in users and users[user]["pd"] == pwd and not users[user]["status"]:
        print("您的账号有问题，请联系管理员!")
    elif user in users and users[user]["pd"] != pwd:
        print("密码错误!")
    else:
        print("用户不存在，请先注册")