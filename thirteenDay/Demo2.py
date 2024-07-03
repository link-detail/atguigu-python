# # 类方法
#
#
# class Player(object):
#
#     numbers = 0
#
#     def __init__(self, name, age):  # 初始化函数
#         self.name = name
#         self.age = age
#         Player.numbers += 1
#
#     # 实例化方法-显示
#
#     def show(self):
#         print("我是荣耀王者的第%d个玩家，我叫%s，我今天%d岁" % (Player.numbers, self.name, self.age))
#
#     @classmethod  # 类方法装饰器
#     def get_players(cls):
#         print("现在荣耀王者的玩家是%d个人" % cls.numbers)
#
#
# mia = Player("mia", 18)
# tom = Player("tom", 21)
# mia.show()
#
#
# Player.get_players()


# # 获取伤害值最大的武器
#
#
# class Weapon(object):
#
#     numbers = 0
#     max_damage = 1000
#     all_weapon = []  # 存放所有武器
#
#     def __init__(self, name, damage, level):  # 初始化函数
#         self.name = name
#         if damage <= Weapon.max_damage:
#             self.damage = damage
#         self.level = level
#         Weapon.numbers += 1
#         Weapon.all_weapon.append(self)  # 存放到列表中
#
#
#     # 选出伤害值最大的武器
#
#     @classmethod
#     def get_max_weapon(cls):
#         max_damage = 0
#         for e in cls.all_weapon:
#             if e.damage > max_damage:
#                 max_damage = e.damage
#
#         for i in cls.all_weapon:
#             if i.damage == max_damage:
#                 return i.name
#
#
#
#
#
# gun1 = Weapon("名刀", 800, "白银")
# gun2 = Weapon("打野", 600, "黄金")
# gun3 = Weapon("邪魔", 999, "铂金")
# gun4 = Weapon("魔忍", 1000, "铂金")
#
# print(Weapon.get_max_weapon())


