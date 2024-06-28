# 生成一个随机字母的列表
import random

list1 = []

# 列表中一共8个元素，每一个元素中有5个字符

for i in range(8):
    str = ""  # 拼接列表中的元素
    for e in range(5):
        result = random.randint(ord("A"), ord("Z"))  # A-Z随机字母
        str += chr(result)
    list1.append(str)

print(list1)
