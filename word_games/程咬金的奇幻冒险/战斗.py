import random as R
CYJ={1:'普攻',2:'爆裂双斧',3:'热烈回旋',4:'正义潜能'}   #技能
SH={1:10,2:10,3:15,4:50}                              #初始伤害
BD={1:0,2:5,3:5,4:15}                                 #自爆被动
DR={1:"狂鸡"}                                         #敌人
DJN={1:{1:'啄',2:'啄',3:'啄',4:'啄'}}                 #敌人技能
DSM={1:30}                                            #敌人生命
DSH={1:{1:5,2:5,3:5,4:5}}                             #敌人伤害
DL={1:{1:'鸡毛',2:'鸡肉',3:'鸡蛋',4:'鸡蛋'}}           #掉落奖励
SM=100
Bag={}
def Add(X,x):
    if x in X:
        X[x]+=1
    else :
        X[x]=1
    return X
while SM>0:
    Zy=R.randint(1,1)                   #选择敌人
    DS=DSM[Zy]
    D=DR[Zy]
    DJ=DJN[Zy]
    DH=DSH[Zy]
    Dl=DL[Zy]
    print('————————————————————')
    print('你遇到了:',D)
    print('')
    while SM>0 and DS>0:                     #战斗
        print('你的生命值:',SM)
        JN=input('请使用技能:')
        if JN in ['1','2','3','4']:
            JN=int(JN)
        else:
            JN=1
        print('')
        print('你使用了',CYJ[JN])
        DS-=SH[JN]
        print(D,'爆了',SH[JN],'血')
        SM-=BD[JN]
        if SM<1:
            SM=1
        print('')
        if DS<=0:
            print(D,'爆了')
            a=R.randint(1,100)
            if 0<a<51:
                dl=Dl[1]
            elif 50<a<81:
                dl=Dl[2]
            elif 80<a<99:
                dl=Dl[3]
            else :
                dl=Dl[4]
            Bag=Add(Bag,dl)
            print(D,'掉落了',dl)
        else:
            DJJ=R.randint(1,4)
            print(D,'使用了',DJ[DJJ])
            SM-=DH[DJJ]
            print('你爆了',DH[DJJ],'血')
            print('')
print('你爆了')
        
                    
                
        
        