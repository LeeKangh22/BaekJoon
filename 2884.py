h,m=map(int,input().split())

for i in range(0,45):
    if m==0:
        h-=1
        m=60
    if h < 0:
        h = 23
    m-=1

print(h, m)