
# 输入

age = input("请输入你的年龄:")

age = int(age) # 类型转换
year = 2024

birthday = year - age

print(birthday)

# 或者是

print("你的生日是%d" % (year - age))

print("你的生日是", birthday, sep="")