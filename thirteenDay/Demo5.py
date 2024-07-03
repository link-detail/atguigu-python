class Player(object):
    numbers = 0
    levels = ["青铜", "白银", "黄金"]

    def __init__(self, name, age, city, level):  # 初始化函数
        self._name = name
        self._age = age
        self._city = city
        if level in Player.levels:
            self._level = level
        else:
            raise Exception("段位设置有误!")
        Player.numbers += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name != self._name:
            self._name = name
        else:
            raise Exception("修改的名字不可以和之前一样！")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            raise Exception("年龄必须是整数!")
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str):
            self._age = city
        else:
            raise Exception("城市修改出错了!")
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level in Player.levels:
            self._level = level
        else:
            raise Exception("段位设置出错！")




mia = Player("mia", 12, "苏州", "白银")
print(mia.name)
mia.name = "tom"
print(mia.name)
print(mia.age)



