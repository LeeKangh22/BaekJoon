import math
N=int(input())
a=[[0]*4 ]*2
b=[]
temp=0
r1=0
r2=0
r3=0
r4=0
for i in range(0,N):
    condition = 0
    for j in range(0,4):
        x,y=map(int,input().split())
        a[0][j]=x
        a[1][j]=y
    r1=math.sqrt((a[0][0]-a[0][1])**2+(a[1][0]-a[1][1])**2)
    r2=math.sqrt((a[0][1]-a[0][2])**2+(a[1][1]-a[1][2])**2)
    r3=math.sqrt((a[0][2]-a[0][3])**2+(a[1][2]-a[1][3])**2)
    r4=math.sqrt((a[0][3]-a[0][0])**2+(a[1][3]-a[1][0])**2)
    r5=math.sqrt((a[0][3]-a[0][1])**2+(a[1][3]-a[1][1])**2)
    r6=math.sqrt((a[0][2]-a[0][0])**2+(a[1][2]-a[1][0])**2)

    b.append(r1)
    b.append(r2)
    b.append(r3)
    b.append(r4)
    b.append(r5)
    b.append(r6)
    b.sort()
    print(b)
    temp=b[0]
    for j in range(1,4):
        if temp==b[j]:
            condition=1
            pass
        else:
            break
    if condition==1:
        for j in range(4,6):
            if temp*math.sqrt(2)==b[j]:
                condition=1
            else:
                break
        if condition==1:
            print(1)
        elif condition==0:
            print(0)


