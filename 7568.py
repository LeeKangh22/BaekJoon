N=int(input())

array=[[0]*N for i in range(2)]
order=[]
rank=1

for i in range(0,N):
    x,y=map(int,input().split())
    array[0][i]=x
    array[1][i]=y

for i in range(0,N):
    rank=1
    for j in range(0,N):
        if array[0][i]<array[0][j] and array[1][i]<array[1][j]:
            rank+=1
    order.append(rank)
for i in range(0,N):
    print(order[i],end=' ')