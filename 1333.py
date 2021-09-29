N,L,D=map(int,input().split())
Dsum=1
sum=1
switch=0
for j in range(0,N):
    for i in range(0,L):
        sum += 1
        Dsum += 1
    for k in range(0,5):
        sum += 1
        Dsum+=1
        if sum==Dsum and Dsum%D==0:
            print(sum)
            exit(0)
while Dsum%D!=0:
    Dsum+=1
print(Dsum)