# 常见标准库
import random

a = random.random()  # 生成随机小数
print(a)

b = random.randint(1, 100)  # 生成随机[1,100]随机整数
print(b)

# 随机展示列表中的元素
list1 = [1, 2, 3, 4, 5, 6]
print(list1[random.randint(0, len(list1)-1)])
print(random.choice(list1))  # 随机显示列表中的元素
print(random.choice("hello"))  # 随机显示字符中的元素
print(random.choice((True, False)))


# 生成一个随机数量字母的列表

list2 = []

print(ord("A"), ord("Z"))  # 获得字母的数字值  A = 65 Z = 90

for i in range(10):
    s = ""
    for i in range(5):
        result = random.randint(ord("a"), ord("z"))  # 大写就是A-Z 小写就是a-z
        s += chr(result)
    list2.append(s)  # 将数字值转为字母

print(list2)

# 打乱列表

list3 = [1, 6, 7, 8, 9]
random.shuffle(list3) # 这个方法没有返回值
print(list3)