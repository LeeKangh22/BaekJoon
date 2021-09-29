import heapq
N,K=map(int(input().split()))
a=[]
for i in range(1,N+1):
    a.append(i)
heapq.heapify(a)
