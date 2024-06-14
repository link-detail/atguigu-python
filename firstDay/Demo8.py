
# 学习回顾


year = 33

print(year)  # 打印

print(end="*")

print(year, "天就可以放假了", sep="")  # 逗号分隔符

month = 2

weather = 75.2

print("今天是%02d月，温度是%.2f" % (month, weather))

# 输入

name = input("请输入你的姓名")

print(type(name))  # 判断数据类型

print(isinstance(name, str))

name = int(name)  # 类型转换

print(type(name))

print(name)