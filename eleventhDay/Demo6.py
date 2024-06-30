# # 正则表达式

import re

# print(re.match(r"^\d+$", "1234"))  # 匹配数字
#
# print(re.match(r"^\w+$", "1234_add_"))  # 匹配数字 字母 下划线
import re

# print(re.match(r"\s+", "   "))  # 匹配空白字符
#
#
# match = re.match(r"^code-\d+\.\w+$", "code-123.txt")  # 匹配任何字符
# print(match)
#
# print(re.match(r"^[1234]+$", "123422"))  # 匹配区间
#
# print(re.match(r"^[^1234]+$", "56789"))  # 不在匹配区间
#
# print(re.match(r"^abcd+$", "abcd"))  # 出现一次或者是多次(必须出现一次)
#
# print(re.match(r"^abcd*$", "abc"))  # 出现0次或者多次（可以不出现）
#
# print(re.match(r"^code{2,4}$", "codeeee"))  # 最多出现指定次数范围
#
# print(re.match(r"^b+|a+", "bbb"))  # 匹配一个即可

# 身份证件验证

# 是十八位数字 后面一位是数字或者是X  前十七位是数字
#
# while True:
#     op = input("请输入你的证件号：")
#     if op[:-1].isdigit() and (op[-1].isdigit() or op[-1] == "X"):
#         print("输入正确！")
#     else:
#         print("输入错误！")


# 341323200303281716
# 正则表达式匹配
#
# pattern = r"^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}([0-9Xx])$"
#
# # 验证出生年月
# print(re.match(pattern, "3|41323|20|03|03|281716"))

# 获取时间

# import time
#
# # print(time.time())  # 时间戳
# #
# time1 = time.localtime()
# print(time1.tm_year)
#
# format = time.strftime("%Y-%m-%d %H:%M:%S", time1)
print(format)


# turtle 库

import turtle
import time

pen = turtle.Turtle()  # 画笔

pen.speed(0)  # 设置速度


# 设计一个电子时钟

pen.back(200)  # 向后移动

# 不断显示
while True:
    time.sleep(1)
    pen.clear()
    time1 = time.localtime()
    time2 = time.strftime("%Y-%m-%d %H:%M:%S", time1)
    pen.write(time2, font=("Arial", 40, "normal"))



input()

















