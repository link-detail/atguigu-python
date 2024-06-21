# 题目要求：输入一个日期，输出这个日期是这一年的第几天  2024-2-21  31+21

date = input("请输入日期：")

days = [31,28,31,30,31,30,31,31,30,31,30,31] # 0, 1, 2

# 分割日期
cut = date.split("-")

# 将前面的日期加起来
total = 0

month = int(cut[1])  # 2
while True:
    total += days[month-3]
    




