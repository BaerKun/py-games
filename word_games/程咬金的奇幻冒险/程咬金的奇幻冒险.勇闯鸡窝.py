import random as R


def ZY():  # 遭遇
    B = ['休']
    a = R.randint(1, 100)
    if 0 < a < 86:
        return '〇'
    elif 85 < a < 96:
        return '斗'
    elif 95 < a < 99:
        return R.choice(B)
    else:
        return '王'


def Add(X, x):  # 添加
    if x in X:
        X[x] += 1
    else:
        X[x] = 1
    return X


def Del(X):  # 清理
    y = []
    for a in X:
        if X[a] == 0:
            y += [a]
    for b in y:
        del X[b]
    return X


CYJ = {1: '普攻', 2: '爆裂双斧', 3: '热烈回旋', 4: '正义潜能'}  # 技能
SH = {1: 10, 2: 10, 3: 15, 4: 50}  # 初始伤害
BD = {1: 0, 2: 5, 3: 5, 4: 15}  # 自爆被动
DR = {1: "狂鸡"}  # 敌人
DJN = {1: {1: '啄', 2: '啄', 3: '啄', 4: '啄'}}  # 敌人技能
DSM = {1: 30}  # 敌人生命
DSH = {1: {1: 5, 2: 5, 3: 5, 4: 5}}  # 敌人伤害
DL = {1: {1: '鸡毛', 2: '鸡肉', 3: '鸡蛋', 4: '鸡蛋'}}  # 掉落奖励
WQ = {'木斧': 10, '瑟斧': 50}  # 图鉴
TO = {}  # 头
XO = {}  # 胸
TU = {}  # 腿
JO = {}  # 脚
FJ = {**TO, **XO, **TU, **JO}  # 防具
SW = {}  # 食物
CL = {}  # 材料
SM = SMax = 100  # 生命/生命上限
GJ = 10  # 攻击
FY = 0  # 防御
To = Xo = Tu = Jo = '无'  # 装备
Wq = '木斧'
Bag = {'瑟斧': 1}  # 背包
WZ = (50, 50)  # 位置
M = {}  # 地图
for x in range(1, 100):
    M[(-1, x)] = M[(0, x)] = M[(100, x)] = M[(101, x)] = M[(x, -1)] = M[(x, 0)] = M[(x, 100)] = M[(x, 101)] = '㏒'
    for y in range(1, 100):
        M[(x, y)] = ZY()
M[(-1, -1)] = M[(-1, 0)] = M[(0, -1)] = M[(0, 0)] = M[(100, 100)] = M[(100, 101)] = M[(101, 100)] = M[(101, 101)] = '㏒'
M[(-1, 100)] = M[(-1, 100)] = M[(0, 100)] = M[(0, 101)] = M[(100, -1)] = M[(100, 0)] = M[(101, -1)] = M[(101, 0)] = '㏒'
while SM > 0:
    x, y = WZ[0], WZ[1]
    print(M[(x - 2, y - 2)], M[(x - 2, y - 1)], M[(x - 2, y)], M[(x - 2, y + 1)], M[(x - 2, y + 2)])
    print(M[(x - 1, y - 2)], M[(x - 1, y - 1)], M[(x - 1, y)], M[(x - 1, y + 1)], M[(x - 1, y + 2)])
    print(M[(x, y - 2)], M[(x, y - 1)], '★', M[(x, y + 1)], M[(x, y + 2)])
    print(M[(x + 1, y - 2)], M[(x + 1, y - 1)], M[(x + 1, y)], M[(x + 1, y + 1)], M[(x + 1, y + 2)])
    print(M[(x + 2, y - 2)], M[(x + 2, y - 1)], M[(x + 2, y)], M[(x + 2, y + 1)], M[(x + 2, y + 2)])
    n = input('选择方向:')
    if n == 's':
        WZ = (x + 1, y)
    elif n == 'a':
        WZ = (x, y - 1)
    elif n == 'd':
        WZ = (x, y + 1)
    else:
        WZ = (x - 1, y)
    if M[WZ] == '㏒':
        WZ = (x, y)
    elif M[WZ] == '斗':
        Zy = R.randint(1, 1)  # 选择敌人
        DS = DSM[Zy]
        D = DR[Zy]
        DJ = DJN[Zy]
        DH = DSH[Zy]
        Dl = DL[Zy]
        print('——————————————————————')
        print('你遇到了:', D)
        print('')
        while SM > 0 and DS > 0:  # 战斗
            print('你的生命值:', SM)
            JN = input('请使用技能:')
            if JN in ['1', '2', '3', '4']:
                JN = int(JN)
            else:
                JN = 1
            print('')
            print('你使用了', CYJ[JN])
            DS -= SH[JN]
            print(D, '爆了', SH[JN], '血')
            SM -= BD[JN]
            if SM < 1:
                SM = 1
            print('')
            if DS <= 0:
                print(D, '爆了')
                a = R.randint(1, 100)
                if 0 < a < 51:
                    dl = Dl[1]
                elif 50 < a < 81:
                    dl = Dl[2]
                elif 80 < a < 99:
                    dl = Dl[3]
                else:
                    dl = Dl[4]
                Bag = Add(Bag, dl)
                print(D, '掉落了', dl)
            else:
                DJJ = R.randint(1, 4)
                print(D, '使用了', DJ[DJJ])
                SM -= DH[DJJ]
                print('你爆了', DH[DJJ], '血')
                print('')
    elif M[WZ] == '休':
        while True:
            print('——————————————————————')
            print('1.打开背包   2.退出')
            J = input('请选择:')
            if J == '1':
                while True:
                    print('——————————————————————————————————————————————————————————')
                    print('头:' + To, '  胸:' + Xo, '  腿:' + Tu, '  脚:' + Jo, '  武器:' + Wq)
                    print('属性:', '生命:' + str(SM) + '/' + str(SMax), '  攻击力:' + str(GJ), '  防御力:' + str(FY))
                    print('背包:', Bag)
                    print('')
                    Bb = input('选择物品(其他键退出):')
                    if Bb in Bag:
                        if Bb in WQ:
                            print('攻击力:', WQ[Bb])
                            a = input('1:装备   其他:退出')
                            if a == '1':
                                Bag = Add(Bag, Wq)
                                Wq = Bb
                                GJ = WQ[Wq]
                                Bag[Wq] -= 1
                                Bag = Del(Bag)
                                SH[1] = GJ
                                SH[2] = 5 + GJ * 0.5
                                SH[3] = GJ * 1.5
                    else:
                        break
            elif J == '2':
                break
    print('——————————————————————')
    M[WZ] = '〇'
print('你爆了')
