# 石头剪刀布 # 你出一个，计算机出一个，三局两胜

import random
for i in range(3):
    plyer_score = 0
    computer_score = 0
    plyer = input("请输入石头剪刀布：")
    computer = random.choice(["石头", "剪刀", "步"])
    print("computer这次出%s" % computer)
    # 判断加分
    if plyer == computer:
        plyer_score += 1
        computer_score += 1
    elif (plyer == "石头" and computer == "剪刀") or (plyer == "剪刀" and computer == "布") or (plyer == "布" and computer == "石头"):
        plyer_score += 1
    else:
        computer_score += 1
    print("玩家得分%d电脑得分%s" % (plyer_score, computer_score))
if plyer_score == computer_score:
    print("平手")
elif plyer_score > computer_score:
    print("玩家赢了")
else:
    print("机器赢了")




