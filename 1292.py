A,B=map(int,input().split())
a=[]
sum=0
for i in range(1,50):
    for j in range(0,i):
        a.append(i)
for i in range(A,B+1):
    sum+=a[i-1]
print(sum)