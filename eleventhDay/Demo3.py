# time库

import time


t1 = time.time()  # 获取时间戳  1970-01-01到今天的秒数
print(t1)

t2 = time.localtime()  # 结构化时间
print(t2.tm_year, t2.tm_mon)

# 格式化时间
t3 = time.strftime("%Y-%m-%d %H:%M:%S", t2)
print(t3)

# turtle库

import turtle

pen = turtle.Turtle()

# pen.speed(0)
#
# for i in range(100):
#     pen.forward(100+i)
#     pen.left(61)
#
# input()


# 设计一个数字小时钟

pen.backward(200)  # 向后200步
pen.speed(0)  # 设置速度

while True:
    time.sleep(1)  # 睡1s
    t1 = time.localtime()
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", t1)
    pen.clear()
    pen.write(t2, font=("Arial", 40, "normal"))





