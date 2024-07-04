# 用户类设计

# 用户类（学生和老师都可以用）

class User(object):

    def __init__(self, name, age, gender, id_number):  # 初始化函数
        # 属性：姓名，年龄，性别，学(工)号,课程信息
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number


    # 显示学生信息
    def show_infos(self):
        print("*" * 15 + "老师（学生信息）" + "*" * 15)
        print("姓名：%s" % self.name)
        print("年龄：%d" % self.age)
        print("性别：%s" % self.gender)
        print("学(工)号：%s" % self.id_number)
        print("*" * 30)







# 学生类
class Student(User):

    def __init__(self, name, age, gender, id_number, curses):  # 初始化函数
        # 属性：姓名，年龄，性别，学号
        super().__init__(name, age, gender, id_number)
        self.curses = curses
    def show_infos(self):
        # 调用父类的方法
        super().show_infos()
        print("课程信息:")
        if not self.curses:
            print("空")
        else:
            for i in self.curses:
                print(i.name)
        print("*" * 15 + "老师（学生信息）" + "*" * 15)


    # 添加课程信息
    def add_curse(self, curse):
        if curse not in self.curses:
            self.curses.append(curse)
        else:
            raise Exception("该学生有这门课程!")
        return True


    # 删除课程信息
    def del_curse(self, curse):
        if curse in self.curses:
            self.curses.remove(curse)
        else:
            raise Exception("该学生没有这门课程!")
        return True


# 老师类（属性：姓名，年龄，性别，工号，是否导员，班级列表）

class Teacher(User):

    def __init__(self, name, age, gender, id_number, dao, cla):
        super().__init__(name, age, gender, id_number)
        self.dao = dao
        self.cla = cla

    def show_infos(self):
        super().show_infos()
        print("是否是辅导员：", ["不是", "是"][self.dao])
        print("班级列表:")
        # 没有班级
        if not self.cla:
            print("暂无班级")
        else:
            for i in self.cla:
                print(i)

jack = Teacher("jack", 50, "男", 5, False, [])
jack.show_infos()

tom = Teacher("tom", 26, "女", 3, True, ["计算机三班", "法律讲解五班"])
tom.show_infos()



