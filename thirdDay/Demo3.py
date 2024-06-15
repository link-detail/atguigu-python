#
# n = 1
#
# while n < 5:
#     n += 1
#     print(n)
#     if n == 4:
#         print("我结束了")
#         break

# 质数：除了1和它本身 不再有其他因数
# n = 13
# i = 2
# flag = 0
# while i < 11:
#     if n%i == 0:
#         print(n, "不是质数")
#         flag = 1
#         break
#     i += 1
# else:
#     print(n, "是质数")

n = 12
flag = 0
for i in range(2, n):
    if n % i == 0:
        print(n, "不是质数")
        break
else:
    print(n, "是质数")
