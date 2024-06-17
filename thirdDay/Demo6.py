# 九九乘法表
"""
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9


.................................9x9=81
"""

n = 9  # 一共9行

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, "x", i, "=", i*j, end=" ")


    print()


print("hello", "liu",  end=" ", sep="m")
print("world", end=" ")