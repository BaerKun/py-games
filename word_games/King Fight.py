import random

print("请你选择你的敌人！")
print("1.亚瑟")
print("2.熊王")
print("3.鸡")
c1 = int(input())
if c1 == 1:
    KK = "亚瑟"
    K = {1: "王斩", 2: "圣撞", 3: "乱砍", 4: "平A"}
elif c1 == 2:
    KK = "熊王"
    K = {1: "掌击", 2: "熊咆", 3: "撕咬", 4: "平A"}
else:
    print("抱歉")
Y = {1: "三拳", 2: "狂笑", 3: "翻跟斗", 4: "平A", 666: "R击"}
YK = {1: 15, 2: 10, 3: 15, 4: 10, 666: -1}
You = 100
King = 100
c4 = 0
c5 = 0
c7 = 0
c8 = 0
while You > 0 and King > 0:
    print("————————————————————————————")
    print(KK, "'s Blood:", King)
    print("You's Blood:", You)
    print("You's 回合")
    if c4 == 1:
        c2 = int(input("You only can 平A(4) —— "))
        c4 = 0
        if c2 != 4:
            print("You RBl!!!")
            c2 = 666
            c8 = 1
    else:
        print("You can use   1.三拳 2.狂笑 3.翻跟斗 4.平A")
        c2 = int(input("请你选择技能："))
    print("")
    print("You use le", Y[c2])
    King -= YK[c2]
    print(KK, "Bao", YK[c2], "Blood")
    if c2 == 2:
        c7 = 1
        print("特殊效果:", KK, "'s 力 is leaving")
    if King <= 0:
        print("You win!")
        break
    print("")
    print(KK, "'s 回合")
    if c8 == 1:
        print(KK, "use 愤怒冲击")
        You -= 200
        print("You Bao Le 200 Blood")
    else:
        c3 = random.randint(1, 4)
        print(KK, "use", K[c3])
        c6 = YK[c3]
        if c5 == 1:
            c6 += 5
            c5 = 0
        if c7 == 1:
            c6 -= 5
            c7 = 0
        You -= c6
        print("You Bao", c6, "Blood")
        if c3 == 2 and KK == "亚瑟":
            c4 = 1
            print("你沉默了")
        elif c3 == 2 and KK == "熊王":
            c5 = 1
            print("Bear King' 力 is Qer")
    if You <= 0:
        print("You Bao Le!")
