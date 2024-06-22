# try 语句

# try:
#     print("hello")
# except:
#     print("如果代码出现了异常，会进入这里！")
#
#
# # try 语句修改
#
# try:
#     a = int(input("请输入-->"))
#     m = 10 / a
#     print(m)
# # as 重新命名
# except ZeroDivisionError as e:
#     print("分母不可以为0！")
#     print("原始报错信息:", e)
#
# except:
#     print("请输入一个数字！")
# else:
#     print("如果没有被except语句捕获，就执行else模块")
# finally:
#     print("无论如何，都会执行finally模块")



# # raise语句（类似于java中的自定义异常处理）
#
# try:
#     pwd = input("请输入你的密码:")
#     if len(pwd) < 8:
#         raise Exception("密码格式有误!")
# except Exception as e:
#     print(e)






# 简单计算器

while True:

    try:
        op = input("请输入一个四则运算式：")
        if "+" in op:
            list1 = op.split("+")
            print(int(list1[0]) + int(list1[1]))
        elif "-" in op:
            list1 = op.split("-")
            print(int(list1[0]) - int(list1[1]))
        elif "*" in op:
            list1 = op.split("*")
            print(int(list1[0]) * int(list1[1]))
        elif "/" in op:
            list1 = op.split("/")
            print(int(list1[0]) / int(list1[1]))
        elif op == "C":
            print("感谢你使用本系统!")
            break
        else:
            raise Exception("请按照1+2格式来输入")


    except ZeroDivisionError:
        print("被除数不可以为0！")
    except Exception as e:
        print(e)


























