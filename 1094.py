X=int(input())
stick=64
rest=X
answer=0
if stick%X==0:
    answer=1
    print(answer)
    exit(0)
else:
    while True:
        if rest<64 and rest>=32:
            answer+=1
            rest-=32
        if rest<32 and rest>=16:
            answer+=1
            rest-=16
        if rest<16 and rest>=8:
            answer+=1
            rest-=8
        if rest<8 and rest>=4:
            answer+=1
            rest-=4
        if rest<4 and rest>=2:
            answer+=1
            rest-=2
        if rest<2 and rest>=1:
            answer+=1
            rest-=1
        if rest==0:break
print(answer)