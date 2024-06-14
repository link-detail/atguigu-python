# total = 10
#
# a = 2
# b = 4
#
# print("a和b一共拿走了", (a+b), "个苹果")
#
# print("c拿了", total - (a+b))

# # 算数运算符
#
# print(10+20)
# print(20-10)
# print(10*20)
# print(20/10)  # 结果是浮点数
# print(9//2)
# print(9 % 2)
# print(2 ** 3)   # 就是2的三次方
#
# # 优先级
#
# print(2+2*3+2**3)


# 赋值运算符

# q = 10
# p = 1
# q += p
# print(q)
#


#
# print(3 == 3.0)  # True
# print("hello" < "i")
#
#
# print(ord("a"))


# # 与 并且 and
# print(1 == 1 and 2 > 1)   # True
# # 短路运算
# print("hello" and "hi")  # hi
# print("" and "hello")    # "" 空
# print(False and "hi")    # False
# print(1 and 0)  # 0
# # 或者 or
# print(1 == 2 or 2 < 1)  # False
# print(1 or 0)  # 1
# print(2023 or 2024 or 0)   # 2023
# print(0 or "" or 888)  # 888
# # 非 not
# print(not True)  # False
# print(not 1)    # False
# print(not "hello")  # False
# print(not "")  # True


# &


print(5 & 7)   # 5

"""
5  101
7  111
101
111
----
101
"""
# |
print(5 | 4)  # 5

"""
5  101
4  100

101
100
----
101
"""

# ^

print(2 ^ 4)

"""
2  10
10
01
101
"""

print(~2)

"""
2  10

1000  左移 10*100 1000
"""
print(2 << 2)  # 8

"""
8  1000
1000  右移位 1000*100 10
"""
print(8 >> 2)  # 2


