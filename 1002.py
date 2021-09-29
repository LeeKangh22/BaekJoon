import math
T=int(input())
len=0
br=0
sr=0
for i in range(0,T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    len=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if r1>=r2:
        br=r1
        sr=r2
    else:
        br=r2
        sr=r1
    if len<r1+r2 and br-sr<len:
        print(2)
    if r1+r2==len or (br-sr==len and (x1!=x2 or y1!=y2)):
        print(1)
    if r1+r2<len or len<br-sr or(x1==x2 and y1==y2 and r1!=r2):
        print(0)
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)


