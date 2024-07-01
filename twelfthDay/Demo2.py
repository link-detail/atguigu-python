# try:
#     with open("hello.txt", encoding="utf8") as f:
#         context = f.read()
#         print(context)
# except Exception as e:
#     print(e)
# else:
#     print("没有出错！")  # 没有出现异常会来这里
# finally:
#     print("代码没有bug！")


# csv文件读取
# import csv
#
# from functools import reduce
# with open("test.csv", mode="r", encoding="utf8") as f:
#     cf = csv.reader(f)
#     head = next(cf)  # 剔除表头(从迭代器里面获取下一个元素)
#     list1 = []
#     for i in cf:
#         list1.append(int(i[2]))
#     print(reduce(lambda a, y : a+y, list1)/len(list1))


# list1 = [1, 3, 4, 6, 7]
#
# iter1 = iter(list1)
#
# print(iter1)
#
# for e in iter1:
#     print(e)

# csv文件写入


# 随机生成信息
# import random
# def random_info():
#     list12 = []
#     for i in range(20):
#         name = ""
#         for i in range(5):
#             random_number = random.randint(ord("A"), ord("Z"))
#             name += chr(random_number)
#         score = random.randint(60, 100)
#         kemu = random.choice(["java", "python", "html", "js"])
#         list1 = [name, kemu, score]
#         list12.append(list1)
#     return list12
#
# import csv
# with open("test.csv", mode="a", encoding="utf8") as f:
#     cf = csv.writer(f)
#     cf.writerows(random_info())


a = 70.67899
print(round(a, 2))



