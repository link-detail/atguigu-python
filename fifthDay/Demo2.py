# # 元组的创建
# tuple =(1, "hello", 2)
# print(tuple)
#
# tuple1 =(1,)  # 元组中只有一个元素的时候，要加一个逗号，区分是int类型还是tuple类型
# print(tuple1)
#
# tuple2 = ()  # 空tuple直接就是空元组
# print(tuple2)
#
# tuple3 = tuple((1, "hello", 3))
# print(tuple3)

# 类型转换

# tuple1 = (1, 2, 3, 4)
# list1 = [1, "hello", 2]
#
#
# tuple2 = tuple("hello")  # str ---> tuple
# print(tuple2)
#
# tuple3 = tuple(list1)    # list ---> tuple
# print(tuple3)
#
# list2 = list(tuple1)  # tuple --> list
# print(list2)
#
# str1 = str(tuple1)    # tuple ---> str
# print(type(str1))
#
# str2 = str(list1)   # list ---> str
# print(str2)
# print(str2[0])


# 常用操作

# 元组索引

#
# tuple2 = ("hello", "nihao", "kiss")
# print(tuple1[0])
#
# # 元组切片
# print(tuple1[::-1])
#
# # 长度
# print(len(tuple1))
#
# # 最大最小
# print(max(tuple1), min(tuple1))
#
# # 删除元组
#
# del tuple1
#
#
# # 加法
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# # 乘法
# print(4 * tuple1)

# tuple1 = (1, 2, 4, 5, 6, 3)
#
# tuple1[0] = 4
#
# print(tuple1.user(3))  # 查找元素数量
#
# print(tuple1.index(3))  # 查找一个元素的索引
#
#
#
# list1 = [1, 3, 4, 6, 7, "hello"]
#
# list1[5] = "nihao"
# print(list1)


tuple1 = [1, 2, 3, 5, 7, 8]

for i in tuple1:
    print(i)

for o in range(len(tuple1)):
    print(tuple1[o])

for i, e in enumerate(tuple1):
    print(i, e)
