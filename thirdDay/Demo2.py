a = 10
match a:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case _:
        print(1111)

print(1 and 0)
print(0 or 1)

a = input("情输入数字")


n = 0
m = 0

while n < 100:
    n += 1
    m += n

print(m)


a = 0
while a < 3:
    print("hello")
    a += 1


for i in range(5):
    print(i)
    print("hello")

print(range(10))


# 1+2+3  i 0 1 2 3
n = 0
m = 0
i = 1

for i in range(3):
    n *= 1
    m += n

print(m)

m = 1
n = 0

for i in range(3):
    m *= (i+1)
    n += m

print(n)

1+1*2+1*2*3
n = 1
m = 1
r = 0
while n < 4:
    m *= n
    r += m
    n += 1

print(r)