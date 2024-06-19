# # range(start, stop, step)  起始位  终止位  步长
#
#
#
#
# n = 153
#
# print(n//100)  # 十位
#
# print((n//10) % 10)
# # 百位
# print(n % 10)  # 个位
#
#
# # 计算100 - 999 有几个水仙花数
#
# # 记录有几个水仙花
# n = 0
#
# for i in range(100, 1000):
#     i1 = i // 100  # 百位
#     i2 = (i//10) % 10  # 十位
#     i3 = i % 10  # 个位
#     if (i1**3)+(i2**3)+(i3**3) == i:
#         print(i, "是水仙花数字", sep="")
#         n += 1
#
# print("100-999中一共有", n, "个水仙花数字")


# str1 = "abcde"
# str2 = "fghi"
#
# print(len(str1))  # 字符串长度
# print(max(str1))  # 最大值
# print(min(str1))  # 最小值
#
# # del str1  # 删除字符串
#
# print("a" in str1)  # 是否包含字符
# print("a" not in str2)  # 是否不包含字符
# print(str1 < str2)  # 比较大小
#
# print(2 * str1)  # 乘法
# print(str1 + str2)  # 加法
#
#
# # 字符串遍历
#
# str3 = "hello"

# for e in str3:
#     print(e)
#
# for i, e in enumerate(str3):
#     print(i , e)
#
# for i in range(len(str3)):
#     print(str3[i])



# 类型转换
#
# n = int("12")
# print(type(n))


# 常用方法
#
# str1 = "hello world"
#
# print(str1.count("l"))  # 某个字符的数量
# print(str1.isupper())   # 字符是否都大写
# print(str1.islower())   # 字符是否都小写
# print(str1)
# print(str1.strip())  # 去除字符串中多余的空格
# print(str1.split(" "))  # 按照指定字符去分割
# print(str1.find("l"))  # 找到某一个字符第一次出现的索引值
# print(str1.find("l", 4))  # 根据起始索引去查找字符出现的索引值
#
#
# str2 = "hello world   "
# print(str2.split(" "))
#
# print(str1.isupper())
#
# print("--".join(["nihao", "hello"]))



# 字母，数字，符号的个数

# str1 = "hello123#$"
#
# a,b,c = 0, 0, 0  # 数字 字母 符号
#
# for i in range(len(str1)):
#     if str1[i].isdigit():
#         a += 1
#     elif str1[i].isalpha():
#         b += 1
#     else:
#         c += 1
#
# print(a, b, c)



# d = {
#     "name": "刘渠好",
#     "age": 21
# }
#
# print(type(d))
# print(d)
#
# d1 = {}
# print(d1)
#
# d2 = dict()
# print(d2)
#
# # 如果定义了重复的键，后面的值会覆盖前面的值
# d3 = {
#     "name": "jack",
#     "age": 12
# }
#
# print(d3)
#
# # 新增
# d3["height"] = 180
#
# # 获取
# print(d3["name"])
#
# # 修改
# d3["name"] = "rose"
#
# del d2  # 删除字典
#
# print(d3)
#
# # in (判断key)
# print("name" in d3)
#
#
# # 字典遍历
#
# # for e in d3:
# #     print(e, d3[e])
# #
# # for i, e in enumerate(d3):
# #     print(e, d3[e])
#
# print(10 * "*")
#
# # 迭代器遍历
#
# print(d3.items())
# for k, v in d3.items():
#     print(k, v)
#
# # 遍历key
#
# for key in d3.keys():
#     print(key)
#
# # 遍历value
#
# for value in d3.values():
#     print(value)


d4 = {
    "name": "jack",
    "age": 12
}

print(d4.pop("name"))  # 删除键

# d5 = d4.copy()  # 拷贝
# print(d5)
#
# print(d4.get("age"))  # 获取对应键值
#
# print(d4)

print(d4.popitem())  # 从后面开始弹出
print(d4)

print(d4.update({"name": "liuquhao"}))  # 更新键值对
print(d4)