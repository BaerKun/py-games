import random as R
def ZY():                  #遭遇
    a=R.randint(1,100)
    if 0<a<86:
        return '〇'
    elif 85<a<96:
        return '斗'
    elif 95<a<99:
        return '休'
    else :
        return '王'
WZ=(50,50)
M={}                                   #地图
for x in range(1,100):
    M[(-1,x)]=M[(0,x)]=M[(100,x)]=M[(101,x)]=M[(x,-1)]=M[(x,0)]=M[(x,100)]=M[(x,101)]='㏒'
    for y in range(1,100):
        M[(x,y)]=ZY()
M[(-1,-1)]=M[(-1,0)]=M[(0,-1)]=M[(0,0)]=M[(100,100)]=M[(100,101)]=M[(101,100)]=M[(101,101)]='㏒'
M[(-1,100)]=M[(-1,100)]=M[(0,100)]=M[(0,101)]=M[(100,-1)]=M[(100,0)]=M[(101,-1)]=M[(101,0)]='㏒'
while True :
    x,y=WZ[0],WZ[1]
    print(M[(x-2,y-2)],M[(x-2,y-1)],M[(x-2,y)],M[(x-2,y+1)],M[(x-2,y+2)])
    print(M[(x-1,y-2)],M[(x-1,y-1)],M[(x-1,y)],M[(x-1,y+1)],M[(x-1,y+2)])
    print(M[(x,y-2)],M[(x,y-1)],'★',M[(x,y+1)],M[(x,y+2)])
    print(M[(x+1,y-2)],M[(x+1,y-1)],M[(x+1,y)],M[(x+1,y+1)],M[(x+1,y+2)])
    print(M[(x+2,y-2)],M[(x+2,y-1)],M[(x+2,y)],M[(x+2,y+1)],M[(x+2,y+2)])
    n=input('选择方向:')
    if n=='s':
        WZ=(x+1,y)
    elif n=='a':
        WZ=(x,y-1)
    elif n=='d':
        WZ=(x,y+1)
    else:
        WZ=(x-1,y)
    if WZ[0]==0 or WZ[0]==100 or WZ[1]==0 or WZ[1]==100:
        WZ=(x,y)
        