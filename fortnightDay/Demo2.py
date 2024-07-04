# 班级类(班级名称，班级号，导员，学生)

import Demo1


class Cla(object):

    def __init__(self, name, id_number, dao, students):  # 初始化函数
        self.name = name
        self.id_number = id_number
        self.dao = dao
        self.students = students


    # 显示班级信息
    def show_cla(self):
        print("*" * 15 + "班级信息" + "*" * 15)
        print("班级名称:%s" % self.name)
        print("班级编号:%d" % self.id_number)
        print("班级导员:%s" % self.dao.name)
        print("班级学生:")
        if not self.students:
            print("暂无学生")
        else:
            for i in self.students:
                print(i.name)
    # 新增学生
    def add_studnet(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            raise Exception("该学生已经在班级里面!")


    # 删除学生
    def del_studnet(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise Exception("该学生不在此班级里!")

mia = Demo1.Student("mia", 21, "女", 1001, ["python初级课程"])
rose = Demo1.Student("rose", 19, "女", 1002, ["java高级课程"])
jack = Demo1.Teacher("jack", 26, "男", 5, True, ["计算机一班", "高数三班"])

math1 = Cla("数学一班", 1002, jack, [mia])

math1.show_cla()

math1.add_studnet(rose)

math1.show_cla()




