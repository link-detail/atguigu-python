
class Demo1:
    name = "jack"

    def __init__(self, age):
        self.age = age
        print(self.name)


mia = Demo1(12)
print(mia.__dict__)