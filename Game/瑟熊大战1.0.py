import random
A=['· ']*25
A[0]='熊'
A[24]='瑟'
S1=1
S2=1
def J(A,x):
    s=0
    for i in A:
        if i==x:
            s+=1
    return s
def B(A,x):
    C=[]
    B=[1,-1,5,-5]
    for a in range(25):
        if A[a]==x and not(a in C):
            random.shuffle(B)
            for b in B:
                if 0<=a+b<25 and A[a+b]!=x:
                    if A[a+b]=='· ':
                        A[a+b]=x
                    else :
                        A[a+b]='· '
                    C+=[a+b]
                    break
    return A
def YX(A):
    B=[]
    for a in range(25):
        if A[a]=='熊':
            B+=[a]
    for b in range(3):
        c=random.choice(B)
        A[c]='瑟'
        B.remove(c)
    return A
while S1!=0 and S2!=0:
    print(A[0],A[1],A[2],A[3],A[4])
    print(A[5],A[6],A[7],A[8],A[9])
    print(A[10],A[11],A[12],A[13],A[14])
    print(A[15],A[16],A[17],A[18],A[19])
    print(A[20],A[21],A[22],A[23],A[24])
    _b_=input('按回车继续/按Y使用技能')
    A=B(A,'熊')
    if _b_=='Y':
        A=YX(A)
    A=B(A,'瑟')
    S1=J(A,'熊')
    S2=J(A,'瑟')
if S1==0:
    print('瑟 Win!')
else :
    print('熊 Win!')          