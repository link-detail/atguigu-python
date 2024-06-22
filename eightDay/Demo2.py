# # 定义函数
# def f():
#     print("hello")
# # 调用函数
# f()
#
#
# def add(a, b):  # 形式参数
#      print(a+b)
#
# add(1,1)  # 实际参数
#
# # return
#
# def add1(n1, n2):
#     return n1+n2
#
# print(add1(1, 3))

# # 位置参数  (参数一一对应)
# def add(a, b):
#     print(a+b)
#
# add(1,2)
#
# # 缺省参数（默认参数） :参数没写就是默认参数，写了就按照实际参数来
# def power(n, m=2):
#     print(n**m)
# power(2)


# def infos(name, age=24, gener="女"):
#     return "我叫%s,今年%d岁，是一名%s生" % (name, age, gener)
#
# mia = infos("mia", 23, "女")
# print(mia)
#
# lily = infos("lily")
# print(lily)
#
# jack = infos("jack", gener="男")
# print(jack)


# 可变参数

# 序列
def add1(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add1(1, 3, 5))  # 可以直接传入元组的方式
list1 = [1, 2, 4]
print(add1(*list1))  # 要是传入一个列表就要加一个*

print(add1(*[1, 5]))


# 字典

def add2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

add2(**{"name" : "jack", "age" : 12})  # 前面也是需要写**