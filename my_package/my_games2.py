# 猜数字小游戏
import random

def games2():
    result = random.randint(1, 10)
    while True:
        guess = int(input("请输入你猜的数字："))
        if guess == result:
            print("恭喜你，猜对了！")
            break
        elif guess > result:
            print("猜大了!")
        else:
            print("猜小了!")

games2()