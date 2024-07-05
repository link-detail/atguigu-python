# 学生类(姓名，年龄，性别，学号）

# 提取一个用户类父类
class User(object):
    def __init__(self, name, age, gender, id_number):  # 初始化函数
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    # 显示学生(老师)信息
    def show_infos(self):
        print("*" * 15 + "老师（学生）信息" + "*" * 15)
        print("姓名:%s" % self.name)
        print("年龄:%d" % self.age)
        print("性别:%s" % self.gender)
        print("学号:%d" % self.id_number)
        print("*" * 15 + "老师（学生）信息" + "*" * 15)






class Student(User):

    def __init__(self, name, age, gender, id_number, curses):  # 初始化函数
        super().__init__(name, age, gender, id_number)
        self.curses = curses

    # 显示学生信息
    def show_student(self):
        super().show_infos()
        print("课程:")
        if not self.curses:
            print("空")
        for i in self.curses:
            print(i.name)

    # 学生添加课程信息

    def add_curse(self, curse):
        if isinstance(curse, Curse) and curse not in self.curses:
            self.curses.append(curse)

        else:
            raise Exception("该学生已经在课程人数中!")
        return True  # 结束一个函数

    # 学生删除课程信息

    def del_curse(self, curse):
        if isinstance(curse, Curse) and curse in self.curses:
            self.curses.remove(curse)
        else:
            print("该学生没有此项课程!")





mia = Student("mia", 18, "女", 1001, [])
#
#
# mia.show_student()


# 老师类(姓名，年龄，性别，工号，是否是导员，班级列表）


class Teacher(User):

    def __init__(self, name, age, gender, id_number, dao, cla):   # 初始化函数
        super().__init__(name, age, gender, id_number)
        self.dao = dao
        self.cla = cla

    # 显示老师信息

    def show_teacher(self):
        super().show_infos()
        print("是否是班主任:%s" % ["不是", "是"][self.dao])
        print("班级列表:")
        if not self.cla:
            print("空")
        else:
            for i in self.cla:
                print(i)
        print("*" * 15 + "老师信息" + "*" * 15)


tom = Teacher("tom", 27, "男", 2001, True, ["法律知识三班"])
#
# tom.show_teacher()



# 班级类（名称，班级号，导员，学生)

class Cla(object):

    def __init__(self, name, id_number, dao, students):  # 初始化函数
        self._name = name
        self.id_number = id_number
        self.dao = dao
        self.students = students



    # 显示班级信息
    def show_Cla(self):
        print("*" * 15 + "班级信息" + "*" * 15)
        print("班级名称:%s" % self._name)
        print("班级班号:%d" % self.id_number)
        print("班级导员:%s" % self.dao.name)
        print("班级学生:")
        if not self.students:
            print("空")
        else:
            for i in self.students:
                print(i.name)

        print("*" * 15 + "班级信息" + "*" * 15)

    # 添加学生

    def add_student(self, student):
        if isinstance(student, Student) and student not in self.students:
            self.students.append(student)
        else:
            raise Exception("添加失败!")

    # 删除学生

    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise Exception("暂无该学生信息！")



# python1 = Cla("python1班级", 3001, tom, [mia])
#
# python1.show_Cla()
#
# rose = Student("rose", 21, "女", 1002)
#
# python1.add_student(rose)
#
# python1.show_Cla()
#
# python1.del_student(mia)
#
# python1.show_Cla()


# 课程类设计(课名，课程id,老师，课程人数，课程容量,课程性质 )


class Curse(object):

    curseList = []

    def __init__(self, name, curse_id, teach, students, capacity, nature):  # 初始化函数
        self.name = name
        self.curse_id = curse_id
        self.teach = teach
        self.students = students
        self.capacity = capacity
        self.nature = nature
        self.now_student = len(self.students)   # 班级现有学生
        self.residual_number = self.capacity - self.now_student  # 课程剩余人数
        Curse.curseList.append(self.name)

    # 显示课程信息
    def show_curse(self):
        print("*" * 15 + "课程信息" + "*" * 15)
        print("课程名字:%s" % self.name)
        print("课程id:%d" % self.curse_id)
        print("课程老师:%s" % self.teach.name)
        print("课程人数:%d" % self.now_student)
        print("课程剩余人数:%d" % self.residual_number)
        print("课程性质:%s" % self.nature)
        print("课程容量:%d" % self.capacity)
        print("课程学生:")
        if not self.students:
            print("空")
        else:
            for e in self.students:
                print(e.name)
        print("*" * 15 + "课程信息" + "*" * 15)

    # 新增学生到课程
    def add_student(self, student):
        if isinstance(student, Student) and student not in self.students and self.residual_number != 0:
            self.students.append(student)
            student.add_curse(self)  # 在学生课程中添加
            self.now_student += 1
            self.residual_number -= 1

        else:
            raise Exception("新增失败！")

    # 课程删除学生
    def del_student(self, student):
        if isinstance(student, Student) and student in self.students:
            self.students.remove(student)
            student.del_curse(self)  # 在学生课程中删除
            self.now_student -= 1
            self.residual_number += 1

        else:
            raise Exception("暂无该学生信息！")

    @classmethod
    def get_all_curse(cls):
        return Curse.curseList

    # 获取课程名字
    @property
    def name(self):
        return self._name

    # 修改名字

    @name.setter
    def name(self, name):
        self._name = name



java123 = Curse("java初级课程", 4001, tom, [], 10, "必修")

print(java123.name)

java123.name = "java高级"

print(java123.name)









