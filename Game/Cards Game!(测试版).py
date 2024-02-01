import random
A=['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4+['RK','QK']
W={"66":-1,"3":0,"4":1,"5":2,"6":3,"7":4,"8":5,"9":6,"10":7,"J":8,"Q":9,"K":10,"A":11,"2":12,"QK":14,"RK":13}
B=["3","4","5","6","7","8","9","10","J","Q","K","A","2","RK","QK","66"]
random.shuffle(A)
Y,XW,YS=[],[],[]
j=1
for i in A:
    o=(j-1)%3+1
    if o==1:
        Y+=[i]
    elif o==2:
        XW+=[i]
    else :
        YS+=[i]
    j+=1
c3,c6,c9="66","66","66"
a,b,c=0,0,0
while Y!=[] and  XW!=[] and YS!=[]:
    c5=[]
    c8=[]
    print("")
    print("You's cards:",Y)
    if a==2:
        c9="66"
        a=0
    else :
        a=0
    c3=input("请你出card:")
    if c3=="66":
        print("You 要不起")
        c3=c9
        b+=1
        c+=1
    elif not(c3 in Y) or W[c3]<=W[c9]:
        print("You RBl!!!")
        break
    else :
        Y.remove(c3)
    if Y==[] :
        print("You win!")
        break
    if b==2:
        c3="66"
        b=0
    else :
        b=0
    for i in range(len(XW)):
        if W[XW[i]]>W[c3]:
            c5+=[W[XW[i]]]
    if c5==[]:
        print("熊王要不起")
        c6=c3
        a+=1
        c+=1
    else :
        c7=min(c5)
        c6=B[c7]
        print("熊王出:",c6)
        XW.remove(c6)
    if XW==[] :
        print("熊王 win!")
        break
    if c==2:
        c6="66"
        c=0
    else :
        c=0
    for i in range(len(YS)):
        if W[YS[i]]>W[c6]:
            c8+=[W[YS[i]]]
    if c8==[]:
        print("亚瑟要不起")
        c9=c6
        a+=1
        b+=1
    else :
        c10=min(c8)
        c9=B[c10]
        print("亚瑟出:",c9)
        YS.remove(c9)
    if YS==[] :
        print("亚瑟 win!")