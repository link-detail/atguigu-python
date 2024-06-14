# # 字符串 索引
#
# str = "hello,world"
#
# print(str[0])   # str[0]  变量名[索引值]
#
# #切片（就是截取）
#
# print(str[0:3])  # str[0:3] 变量名字[首索引:尾索引]  结果是包头不包尾
#
# print(str[0:5:2]) # str[0:3:2] 变量名字[首索引:尾索引:步数]  结果是包头不包尾

#
# 进行字符转反转

# n1 = "cat"
#
# print(n1[-1:-4:-1])
#
# # n2 = n1[-1:4]
# #
# # print(n2)  # tac
#
# n2 = "hello"
#
# print(n2[::])


# 数据类型转换

# # int()
# # 整数--->int
# str = "234"
# n= int(str)
# print(n)
#
# # 浮点数-->int
# n1 = 3.63
# n1 =int(n1)
# print(n1)
#
# # 布尔值-->int

# print(int(a),int(b))


# float

# n1 = "1.9"
# print(float(n1))
#
# n2 = 12
# print(float(n2))
#
# a= True
# b= False
# print(float(a), float(b))

# bool
# a = "aa"
# b = ""
# print(bool(a), bool(b))  # 字符串有内容就是True，没有内容就是False
#
# c = 1
# d = 0
# print(bool(c), bool(d))  # 大于0的数字都是True
#
# e = 5.0
# f = 0.0
# print(bool(e), bool(f))

# str

# a = 1
# a = str(a)
# print(type(a))
# print(str(a))
#
# b = 2.0
# b= str(b)
# print(type(b))
# print(str(b))
#
# c = True
# d = False
# c = str(c)
# d = str(d)
# print(type(c), type(d))
# print(str(c), str(d))


# 进制的转换

a = "10"
print(int(a, 2))

b = "1b"
print(int(b, 16))

a = 278

b = 278

print(id(a), id(b))


