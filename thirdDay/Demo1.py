# # 单分支
# weather = "下雨"
# if weather == "下雨":
#     print("要带雨伞")
#
#
# # 双分支
# # a = int(input("请输入你的数字:"))
# if a >= 1:
#     print("我大于1了")
# else:
#     print("我小于1了")


# 多分支
#
# number = int(input("请输入你的成绩:"))
#
# if number > 90:
#     print("A")
# elif number > 80 & number < 90:
#     print("B")
# elif number > 70 & number < 80:
#     print("C")
# else:
#     print("D")
#
#
# a = 3
# if a > 1:
#     print("hello")
#     if a > 2:
#         print("world")


weight = int(input("请输入你的体重:"))
high = float(input("请输入你的身高:"))

bmi = weight/(high**2)
if bmi < 18.5:
    print("过瘦")
elif bmi > 18.5 and bmi < 23.9:
    print("正常")
elif bmi > 23.9:
    print("过胖")
else:
    print("不符合BMI测试")

