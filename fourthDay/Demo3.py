# 九九乘法表

"""
1 * 1
1 * 2 2 * 2
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "x", i, "=", (i*j), end=" ")
    print()

ye = 1

print("%d" %(ye))