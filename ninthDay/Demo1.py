# # 变量的作用域
#
# num1 = 1  # 全局变量
#
# def add1():
#     global num1  # 声明这个变量是全局变量
#     num1 = 2  # 局部变量（只在方法里面有效，出了方法之后就无效了，在方法中调用之后就被销毁了）
#     print(num1)
#
# add1()  # 2
#
# print(num1)
#
#
# # 可变类型和不可变类型
#
# list1 = [1, 3, 5, 7]
#
# def change():
#     list1[0] = 6
#     print(list1)
#
# change()
#
# print(list1)
from functools import reduce

# 匿名函数
# a = lambda x, y: x+y  # 后面的x+y代表就是 return x+y
#
# print(a(1, 3))
#
#
# # map函数
#
# # 之前的列表平方处理
#
# list1 = [1, 2, 3, 4]
# for e in range(len(list1)):
#     list1[e] = list1[e]**2
#
# print(list1)
#
# # map函数处理
#
# list2 = [1, 3, 5, 7]
# def a(b):
#     return b**2
#
# print(list(map(a, list2)))  # 将list2中的每一个函数执行方法a，并将更新结果放在元素位置上
#
#
# # map函数+匿名函数处理
#
# print(list(map(lambda a: a**2, list2)))


# # reduce 函数  累加
#
# from functools import reduce  # reduce不在内置库里面，需要导入
#
# list1 = [1, 3, 5, 6, 8, 10]
#
# print(reduce(lambda a,b: a+b, list1))
#
#
# # filter 过滤函数
#
# print(list(filter(lambda a: a % 2 == 0, list1)))

# 去除列表中的非0元素
#
# a = [1, 8, 9, 0, 2, 0, 4]
#
# print(list(filter(lambda b: b ** 2 != 0, a)))
#
# # 将列表中的元素直接变成数字
#
# b = [1, 8, 9, 0, 2, 0, 4, 3]
#
# print(int(reduce(lambda x,y: str(x)+str(y), b)))
#
#
#
#
#
# print("hello" + "world")





# # 常见内置函数
#
# print(abs(-10))  # 绝对值
# print(bool(0))  # 对传入参数取布尔值
# print(bin(10))  # 接收一个十进制，转为二进制  （0b）1010
# print(oct(65))  # 接收一个十进制，转为八进制  （0o）101
# print(hex(17))  # 接收一个十进制，转为十六进制  （0x）11
# print(str(12))  # 转字符串
# print(type(str(12)))
#
# print(chr(65))  # 数字转字符，查看ascii码表
# print(ord("A"))  # 字母转数字，查看ascii码表
#
# a = lambda b: b+1
# print(eval("a(1)"))  # 执行python代码，并返回执行结果
#
# a = 1
# print(dir(a))  # 接收对象作为参数，返回该对象的所有属性


# 递归函数 (函数自己调用自己)

# 2阶楼梯
# 1 1
# 2

# 3阶楼梯，每次走一个或者是两个，有多少中走法
# 1 1 1
# 1 2
# 2 1

# 4阶楼梯
# 1 1 1 1
# 1 1 2
# 2 1 1
# 2 2
# 1 2 1

# 总结 f(n)= f(n-1)+f(n-2)  (先把临界情况算好，之后套用公式)

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n-1)+f(n-2)


print(f(4))

for i in range(10):
    print("%d个阶梯有%d个走法" %(i, f(i)))



# 遍历实现递归

list1 = [0, 1, 2]

print(list1[-1])
for i in range(11):
    if i > 2:
        result = list1[i-1] + list1[i-2]
        list1.append(result)

print(list1)















