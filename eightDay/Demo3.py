# # 简单计算器
# while True:
#     opt = input("请输入一个四则运算式-->")
#     try:
#         if "+" in opt:
#             a = opt.split("+")
#             print(int(a[0]) + int(a[1]))
#         elif "-" in opt:
#             a = opt.split("-")
#             print(int(a[0]) - int(a[1]))
#         elif "x" in opt:
#             a = opt.split("x")
#             print(int(a[0]) * int(a[1]))
#         elif "/" in opt:
#             a = opt.split("/")
#             print(int(a[0]) / int(a[1]))
#         elif "C" in opt:
#             print("感谢你使用我的计算器！")
#             break
#         else:
#             raise Exception("你的四则运算式子有误！")
#
#     except ZeroDivisionError as e:
#         print("被除数不可以是0！", e)
#     except Exception as e:
#         print(e)

# 默认参数

def infos(name, age=18, gender="男"):
    print("我的名字是%s，年龄%d，性别%s" %(name, age, gender))

infos("jack", 18, "男")

infos("lily", 19)

infos("rose", gender="女")

# 可变参数

def add1(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

dict1 = {"name":"jack","age":19}
add1(**dict1)

# 集合
def add2(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
set1 = {1, 2, 3}
add2(*set1)