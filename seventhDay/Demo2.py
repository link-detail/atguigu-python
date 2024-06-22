# 题目要求：输入一个日期，输出这个日期是这一年的第几天  2000-3-21  31+29+21=81 53 2001-2-21 31+28+21=80

date = input("请输入日期：")

days = [31,28,31,30,31,30,31,31,30,31,30,31]  # 闰年 2：29


# 分割日期
list1 = date.split("-")

# 判断是闰年还是平年
year = int(list1[0])

if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    days[1] = 29

# 计算之前的全部日期
month = int(list1[1])

total = 0

for i in range(month-1):
    total += days[i]

total += int(list1[2])

print(total)





    




