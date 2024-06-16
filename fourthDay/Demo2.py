# 打印出m行n列的图形

# m = int(input("晴输入行数"))
# n = int(input("请输入列数"))
#
# for i in range(m):
#     print(n * "*")


# m = 4
# n = 5
#
# for i in range(m):
#     for i in range(n):
#         print("*", end="")
#     print()



# 打印出n行三角形

# n = 5
#
# for i in range(n):
#     print((n - (i+1)) * " " + (2*i+1) * "*")


# 穷举

peach = 1  # 假设就买了一个桃子

while True:
    d1 = peach//2 - 1  # 第一天剩的
    d2 = d1//2 - 1     # 第二天剩的
    d3 = d2//2 - 1     # 第三天剩的
    if d3 == 1:
        print(peach)
        break
    peach += 1






