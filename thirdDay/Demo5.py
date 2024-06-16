# 判断一个数字是否是质数  （除了1和本身就没有其他可以整除的了）



# for i in range(2, n):
#     if n % i == 0:
#         print(n, "不是质数")
#         break
# else:
#     print(n, "是质数")
m = 2
n = 11
flag = 1
while m < n:
    if n % m == 0:
        print(n, "不是质数")
        flag = 0
        break
    m += 1
if flag == 1:
    print(n, "是质数")