# 正则表达式
import re

# 匹配纯数字[0-9]  \d+ 是连续匹配 要是中间有个123*456中间有一个非数字 到*这里就不匹配了 匹配到 123
a = re.match(r"\d+", "123*456")
print(a)

# 匹配数字 字母 下划线 同上匹配准则  ^:匹配开头 $:匹配结尾（要是结尾和开头不符合匹配准则，就没有匹配结果返回None）
b = re.match(r"^\w+$", "_23er_")
print(b)

# 匹配空白字符
c = re.match(r"\s+", "  ")
print(c)

# . 任意字符(\d \s \w)  $结尾匹配的准则是和他的上一位匹配准则一样  ^code：如果是这样就是固定的开头匹配code
d = re.match(r"^code\d+-\d+-\d+$", "code2-2-12")
print(d)

# [] 在区间内  ^[abcd]+$:意思是开头和结尾匹配都是按照哦[]区间来的
e = re.match("^[abcd]+$", "abcd")
print(e)

# [^] 不在区间内  ^
e = re.match("^[^abcd]+", "hjjdhjkd")
print(e)

# * 最后一个可以出现也可以不出现(0次或者一次)
f = re.match(r"^abcc*$", "abc")
print(f)

# + 最后一个必须出现一次或者是多次
f1 = re.match(r"^abcc+$", "abccc")
print(f1)

# {} 最后一个可以出现多少次 {2}:2次  {2, 5}：两次或者是五次
g = re.match(r"^abc{2,5}$", "abccccc")
print(g)

# | 或者  匹配其中一个即可
h = re.match(r"^a|b$", "b")
print(h)




