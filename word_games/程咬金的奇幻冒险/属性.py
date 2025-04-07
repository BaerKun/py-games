def Del(X):                          #清理
    y=[]
    for a in X:
        if X[a]==0:
            y+=[a]
    for b in y:
        del X[b]
    return X
def Add(X,x):                        #添加
    if x in X:
        X[x]+=1
    else :
        X[x]=1
    return X
def Num_is(x):
    try:
        x=float(x)
        return True
    except:
        return False
Bag={'鸡毛':10}
FJ={'鸡毛靴'}
ZB={1:['鸡毛头盔','鸡毛',5,5],2:['鸡毛胸甲','鸡毛',8,8],3:['鸡毛护腿','鸡毛',7,7],4:['鸡毛靴','鸡毛',4,4],5:['鸡腿棒','鸡肉',10,20]}
while True:
    print('1.装备  2.食物  3.材料  4.退出')
    x=input('请您选择:')
    while x=='1':
        print('图纸：')
        for a in range(1,len(ZB)+1):
            b=ZB[a]
            print(str(a)+'.'+b[0]+'：'+b[1]+'*'+str(b[2]))
        y=input('请您选择(其他键退出):')
        try:
            y=int(y)
            if 0<y<=len(ZB):
                z=ZB[y]
                if z[0] in FJ:
                    print(z[0]+'：防御力'+str(z[3]))
                else:
                    print(z[0]+'：攻击力'+str(z[3]))
                print('1.打造  ')
                n=input('请选择(其他键退出):')
                if n=='1':
                    if (z[1] in Bag) and (Bag[z[1]] >=z[2]):
                        Bag[z[1]]-=z[2]
                        Bag=Add(Del(Bag),z[0])
                    else:
                        print('材料不够!')
            else:
                break
        except:
            break
    while x=='2':
        print('食谱：')
        print('1.煎蛋：鸡蛋*1')
        print('2.烤肉：鸡肉*1')
    while x=='3':
        print('')
    if x=='4':
        break
    

