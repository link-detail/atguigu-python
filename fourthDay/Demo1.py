for i in range(5):
    if i == 2:
        continue
    print(i)

a = 1

if a == 1:
    pass


# 指数爆炸

# 纸的厚度

n = 0.1
w = n
for i in range(50):
    w *= 2
    print(w)

# 国王数麦粒

# 1:1 2:2 3:4 4:8 5:16


# 50个格子
m = 1
n = 0
for i in range(1, 5):
    m *= 2
    if i == 1:
        m = 1
    n += m
    print("第", i, "个格子有", m, "个")
print("50个格子里面有", n, "个麦粒")


print(2 << 3)

print(8 >> 2)


# 人生的复利 1+0.01

n = 1
m = 1
s = 0

while n <= 100:
    m += 0.1
    s += m
    n += 1
print(s)