# 猜数字下游戏
import random

guess = random.randint(1, 100)

while True:
    plyer = int(input("请输入你猜的数字:"))
    if plyer > guess:
        print("猜大了！")
    elif plyer < guess:
        print("猜小了")
    else:
        print("猜对了！")
        break