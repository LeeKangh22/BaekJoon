temp=0
while True:
    try:
        n,k=map(int,input().split())
        chicken=n
        mod=0
        while True:
            if n < k:
                print(chicken)
                break
            else:
                if mod > k:
                    temp+=1
                    mod -= k
                mod += int(n % k)
                n = int(n / k)
                chicken += n
                chicken += temp
    except EOFError:
        break