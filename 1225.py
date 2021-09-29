A,B=map(str,input().split())
Am=0
Bm=0
for i in range(0,len(A)):
    Am+=int(A[i])
for j in range(0,len(B)):
    Bm+=int(B[j])
print(Am*Bm)