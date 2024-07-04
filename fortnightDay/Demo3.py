# 课程类(属性：科名，课程id，老师，学生列表，课程性质，课程容量)


import Demo1, Demo2

class Course(object):


    courseList = []  # 课程列表

    def __init__(self, name, id_number, teach, students, nature, capacity):  # 初始化函数
        self._name = name
        self.id_number = id_number
        self.teach = teach
        self.students = students
        self.nature = nature
        self.capacity = capacity
        self.now_numbers = len(self.students)  # 现有人数
        self.residual_numbers = self.capacity - self.now_numbers  # 课程剩余人数
        Course.courseList.append(self.name)


    # 封装获取课程名字
    @property
    def  name(self):
        return self._name
    # 封装修改课程名字

    @name.setter
    def name(self, name):
        if not name:
            raise Exception("课程名字不可以为空!")
        if not isinstance(name, str):
            raise Exception("课程名称类型必须是字符串!")
        self._name = name

    # 显示课程信息
    def show_curse_info(self):
        print("*" * 15 + "课程信息" + "*" * 15)
        print("课程名称:%s" % self._name)
        print("课程编号:%d" % self.id_number)
        print("授课老师:%s" % self.teach.name)
        print("课程性质:%s" % self.nature)
        print("课程容量:%d" % self.capacity)
        print("课程现有人数:%d" % self.now_numbers)
        print("课程剩余人数:%d" % self.residual_numbers)
        print("课程学生:")
        if not self.students:
            print("空")
        else:
            for i in self.students:
                print(i.name)

        print("*" * 15 + "课程信息" + "*" * 15)

    # 添加学生

    def add_student(self, student):
        if student in self.students:
            raise Exception("该同学已经在此课程中!")
        elif self.residual_numbers == 0:
            raise Exception("该课程已经报满，请换一个课程吧!")
        self.students.append(student)
        # 在学生课程信息新增
        student.add_curse(self)
        self.now_numbers += 1  # 课程报名人数+1
        self.residual_numbers -= 1  # 课程剩余人数-1
        return True


    # 删除学生

    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
            # 将学生的课程信息也删除
            student.del_curse(self)
        else:
            raise Exception("该学生不在本课程内！")
        self.now_numbers -= 1  # 课程报名人数+1
        self.residual_numbers += 1  # 课程剩余人数-1
        return True

    # 获取所有课程信息
    @classmethod
    def get_all_course(cls):
        return cls.courseList

# 学生
mia = Demo1.Student("mia", 21, "女", 1001, [])

rose = Demo1.Student("rose", 19, "女", 1002, [])

# 老师
jack = Demo1.Teacher("jack", 28,"男", 6001, True, ["计算机一班"])

# 课程
python1 = Course("python高级课程", 7001, jack, [mia], "必修课", 10)
python2 = Course("python初级课程", 7002, jack, [mia, rose], "选修课", 20)

python1.name = ""
python1.show_curse_info()
print(python1.__dict__)











