#
# list1 = list("12345689")
#
# list2 = ["hello", 1, 2.9]
#
# # 列表索引
# print(list1[0])
# print(list1[-1])
#
# # 列表切片
# print(list1[0:2])
# print(list1[::-1])
#
# # 列表加法 乘法
# print(list2 + list1)
# print(list1 * 2)
#
# # 列表的成员运算
# print("1" in list1)
# print("1" not in list1)
# print(list1 > list2)

# print(len(list1))  # 列表长度
# print(max(list1))  # 列表最大值
# print(min(list1))  # 列表最小值
#
# del list1  # 删除列表


# 列表的遍历
# 第一种
# for i in range(len(list1)):
#     print(list1[i])
#
#
# print(6 * "*")
#
# # 第二种
#
# for i in list1:
#     print(i)
#
# print(6 * "*")
#
# # 第三种
# for i, e in enumerate(list1):  # i:索引  e:索引对应元素
#     print(i, e)

list = [1, 2, 3, 4, 5]
print(list)
#
# # 追加元素
# list.append("key")
# print(list)
#
# # 追加集合
# list.extend(["hao", "huai"])
# print(list)
#
# # 插入元素
# list.insert(1, "你好")
# print(list)


# 删除（弹出）元素
# list.pop(0)
# print(list)
#
# # 根据值删除
# list.remove(2)
# print(list)
#
# # 查看一个元素在列表中的索引
# list1 = list.index(3)
# print(list1)
#
# # 元素在列表中有几个
# print(list.count(1))
#
#
# # 清空列表
# list.clear()
# print(list)

# 计算n个人的平均年龄

list = [18, 20, 19, 26, 27]
n = 0

for e in list:
    n += e

print(n / len(list))
