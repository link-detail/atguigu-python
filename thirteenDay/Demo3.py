# 静态方法

# class Player(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def invalid(**kwargs):
#         if kwargs["age"] > 18:
#             return True
#         else:
#             print("请重试！")
#
# infos = {"name": "mia", "age": 18}
# Player.invalid(**infos)  # 静态方法校验
# mia = Player("mia", 19)



# 继承

#
# # 父类
# class Player(object):
#
#     def __init__(self, name, age):  # 初始化函数
#         self.name = name
#         self.age = age
#
#     # 实例方法
#     def show(self):
#         print("我叫%s，今天%d岁" % (self.name, self.age))
#
#
#
# # 自类
#
# class Vip(Player):
#
#     # 子类构造函数
#     def __init__(self, name, age, coin):
#         # 调用父类的构造函数
#         super().__init__(name, age)
#         # 子类独有的属性
#         self.coin = coin
#
#     # 子类重写父类的方法
#     def show(self):
#         print("我叫%s，今年%d岁，卡里还有%d钱" %(self.name, self.age, self.coin))
#
#
# vip1 = Vip("mia", 19, 100)
#
#
# vip1.show()
#
# # 判断类型
# print(type(vip1))
# print(isinstance(vip1, Player))
# print(isinstance(vip1, Vip))


# 多态



class Animal(object):
    def speak(self):
        print("动物的叫声")

class Cat(Animal):
    def speak(self):
        print("喵喵")

class Dog(Animal):
    def speak(self):
        print("旺旺")

def speak(object):
    object.speak()

kitty = Cat()
puppy = Dog()
animal = Animal()
# animal.speak()
# kitty.speak()
# puppy.speak()

speak(kitty)
speak(puppy)
speak(animal)















