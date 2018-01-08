import random
computar=["石头","剪刀","布"]
gess = 1
i=0
j=0
while gess:
    n=random.randint(0,2)
    m=int(input("请输入（0，1，2）:"))
    if m!=0 and m!=1 and m!=2:
        print("游戏结束")
        break
    else:
        print("玩家:",computar[m])
        print("电脑:",computar[n])
        if n==m:
            print("平局")

        else:
            if n<m:
                if n==0 and m==2:
                    print("玩家赢")
                    j += 1
                    print("玩家加分")
                    print("玩家积分：", j)
                print("电脑赢")
                i+=1
                print("电脑加分")
                print("电脑积分：",i)
            if n>m:
                if n==2 and m==0:
                    print("电脑赢")
                    i += 1
                    print("电脑加分")
                    print("电脑积分：", i)
                print("玩家赢")
                j+=1
                print("玩家加分")
                print("玩家积分：",j)
if i==j:
    print("---平局---")
    print("玩家得分为：", j, "电脑得分为：", i)
else:
    if i<j:
        print("最终玩家胜利")
        print("玩家得分为：",j,"电脑得分为：",i)
    else:
        print("最终电脑胜利")
        print("玩家得分为：",j,"电脑得分为：",i)