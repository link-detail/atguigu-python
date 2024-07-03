# # 封装
#
# class Player(object):
#
#     def __init__(self, name, age):
#         self._name = name  # _name  表示受保护的属性  :_
#         self.__age = age   # __age 表示私有属性 :__
#
#      # _show:受保护的方法  __show:私有方法
#     def __show(self):  # 私有属性在类外面不可以被使用，但是在类里面还是可以被使用的
#         print("我的名字是%s，我今年%d岁" % (self._name, self.__age))
#
# mia = Player("mia", 12)
# mia._name = "tom"  # _这个下划线就好比是一个标识，表示这个属性是受保护的，不要随意更改，要是更改的话还是可以的
# print(mia._name)
# # print(mia.__age)  # __是私有属性，这个是不可以查看的
#
# mia._Player__show()
#
#
# # 查询封装本质（其实__age这个属性名字被改为了_Player__age了）
#
# print(mia.__dict__)  # 打印对象的属性和属性值
# print(mia._Player__age)
#
# print(dir(mia))  # 查看对象的属性和方法



# 把参数修改放到类里面，不在外面被随便修改


class Player(object):

    def __init__(self, name, age):
        self._name = name  # _name  表示受保护的属性  :_
        self.__age = age   # __age 表示私有属性 :__

     # _show:受保护的方法  __show:私有方法
    def __show(self):  # 私有属性在类外面不可以被使用，但是在类里面还是可以被使用的
        print("我的名字是%s，我今年%d岁" % (self._name, self.__age))

    # 查看年龄
    @property  # 获取变量
    def age(self):
        return self.__age

    # 修改年龄
    @age.setter  # 修改变量 age前面获取变量的方法名
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise Exception("年龄只可以是整数！")

mia = Player("mia", 19)
print(mia.age)

mia.age = 22
print(mia.age)



















