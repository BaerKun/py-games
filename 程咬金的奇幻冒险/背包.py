To=Xo=Tu=Jo='无'
Wq='木斧'
SM=SMax=100
GJ=10
FY=0
Bag={'鸡毛':23,'鸡蛋':322,'鸡肉':22,'瑟斧':1}
WQ={'木斧':10,'瑟斧':50}
def Del(X):
    y=[]
    for a in X:
        if X[a]==0:
            y+=[a]
    for b in y:
        del X[b]
    return X
def Add(X,x):
    if x in X:
        X[x]+=1
    else :
        X[x]=1
    return X
while True:
    print('——————————————————————————————————————————————————————————')
    print('头:'+To,'  胸:'+Xo,'  腿:'+Tu,'  脚:'+Jo,'  武器:'+Wq)
    print('属性:','生命:'+str(SM)+'/'+str(SMax),'  攻击力:'+str(GJ),'  防御力:'+str(FY))
    print('背包:',Bag)
    print('')
    Bb=input('选择物品(其他键退出):')
    if Bb in Bag:
        if Bb in WQ:
            print('攻击力:',WQ[Bb])
            a=int(input('1:装备   其他:退出'))
            if a==1:
                Bag=Add(Bag,Wq)
                Wq=Bb
                GJ=WQ[Wq]
                Bag[Wq]-=1
                Bag=Del(Bag)
    else :
        break