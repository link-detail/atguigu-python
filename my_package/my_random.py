
import random

# 生成随机字符
def random_char(upper=True):
    if upper:
        result = random.randint(ord("A"), ord("Z"))
    else:
        result = random.randint(ord("a"), ord("z"))
    return result


# 将随机字符拼接起来
def link_char(length):
    list1 = []
    s = ""
    for i2 in range(length):
        result = chr(random_char(random.choice([True, False])))
        s += result
    list1.append(s)
    return list1


print(link_char(4))






