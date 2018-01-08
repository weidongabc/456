import random
secret=random.randint(1,100)
guess=0
while guess != secret:
    temp=input("猜数字游戏")
    guess=int(temp)
    if guess >secret:
        print("太大了！")
    else:
        print("太小了！")
    if guess==secret:
        print("恭喜答对了！没奖励")
        print("游戏结束")
