razor = list(input())
stick = []
answer = 0

for i in range(len(razor)):
    if razor[i] == '(':
        stick.append('(')
    else:
        if razor[i - 1] == '(':
            stick.pop()
            answer += len(stick)
        else:
            stick.pop()
            answer += 1
print(answer)