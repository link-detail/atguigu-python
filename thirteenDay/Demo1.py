# # 类的创建
#
# class Player(object):  # object 基类
#     pass
#
# tom = Player()  # 类的实例化（创建对象）
# print(type(tom))
#
# print(isinstance(tom, Player))  # 判断一个对象是否属于一个基类

# 实例属性

# class Player(object):
#     def __init__(self, name, age, city): # 初始化操作（构造函数）
#         self.name = name  # 类的属性
#         self.age = age
#         self.city = city
#
# mia = Player("mia", 12, "安徽")  # 创建实例（对象）
# mia.city = "杭州"  # 修改属性
# print(mia.name, mia.age, mia.city)
#
# print(mia.__dict__)  # 获取一个对象的所有属性及其属性值

# 武器

# class Cut(object):
#     def __init__(self, name, attack, level):  # 初始化函数
#         self.name = name
#         self.attack = attack
#         self.level = level
#
#
# # 名刀
#
# famousSword = Cut("名刀", 1000, "一级")
#
# print(famousSword.__dict__)  # 查看一个实例的属性及其属性值

# 类属性

# class Player(object):
#     numbers = 0  # 类的属性
#     def __init__(self, name, age):  # 初始化函数
#         self.name = name
#         self.age = age
#         Player.numbers += 1  # 类属性
#
# mia = Player("mia", 18)
# tom = Player("tom", 12)
#
# print("荣耀王者欢迎第%d个玩家注册" % Player.numbers)

# 武器：名字，伤害值，等级

class Weapon(object):

    numbers = 0  # 记录创建武器数
    max_damage = 10000
    levels = ["青铜", "白银", "黄金", "钻石"]

    def __init__(self, name, damage, level):  # 初始化函数
        self.name = name
        self.damage = damage
        self.level = level
        Weapon.numbers += 1
        if damage>Weapon.max_damage:
            raise Exception("武器最大值不能超过20000！")
        if level not in Weapon.levels:
            raise Exception("武器登记有误！")

    # 实例化方法-显示武器属性
    def show_weapon(self):
        for k , v in self.__dict__.items():
            print(k, v)


try:
    famousKnief = Weapon("名刀", 20000, "白银")
    print(Weapon.numbers)
except Exception as e:
    print(e)


# 实例方法

class Player(object):
    numbers = 0
    levels = ["青铜", "白银", "黄金", "钻石", "王者"]

    def __init__(self, name, age, city, level):  # 初始化参数
        self.name = name
        self.age = age
        self.city = city
        Player.numbers += 1
        if level in Player.levels:
            self.level = level
        else:
            raise Exception("段位设置不符!")

    # 实例方法-显示
    def show(self):
        print("我是荣耀王者的第%d个玩家，我来自%s，段位是%s" %(Player.numbers, self.city, self.level))


    # 实例化方法-段位升级
    def level_up(self):
        index = Player.levels.index(self.level)  # 获取当前段位索引数字
        if index < len(Player.levels)-1:  # 可以升级
            index += 1
            self.level = Player.levels[index]
         
         
    # 实例化方法-获取武器
    
    def get_weapon(self, Weapon):
        self.Weapon = Weapon

    # 实例化对象-获取对象武器属性
    def show_weapon1(self):
        return self.Weapon.show_weapon()


        




mia = Player("mia", 18, "安徽", "白银")
mia.show()

mia.level_up()

mia.show()
mia.level_up()

mia.show()
mia.level_up()

mia.show()
mia.level_up()

mia.show()

gun = Weapon("名刀", 1000, "白银")
mia.get_weapon(gun)
mia.show_weapon1()
















































