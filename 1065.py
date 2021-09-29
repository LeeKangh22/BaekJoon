N=input()
count=0
switch=1
j=1
if len(N)>=3:
    count=99
    for i in range(100, int(N) + 1):
        N=str(i)
        switch = 1
        if int(N[j]) - int(N[j-1]) == int(N[j + 1]) - int(N[j]) :
            switch =1
        else:
            switch = 0
        if switch==1:
            count+=1
    print(count)
elif int(N)<100:
    print(int(N))

