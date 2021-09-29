N=int(input())
aver=0
grade = 0
g_sum = 0
for i in range(0,N):
    A, B, C = input().split()
    g_sum += int(B)
    if C == "A+":
        grade += int(B)*4.3
    elif C == "A0":
        grade += int(B)*4.0
    elif C == "A-":
        grade += int(B)*3.7
    elif C == "B+":
        grade += int(B)*3.3
    elif C == "B0":
        grade += int(B)*3.0
    elif C == "B-":
        grade += int(B)*2.7
    elif C == "C+":
        grade += int(B)*2.3
    elif C == "C0":
        grade += int(B)*2.0
    elif C == "C-":
        grade += int(B)*1.7
    elif C == "D+":
        grade += int(B)*1.3
    elif C == "D0":
        grade += int(B)*1.0
    elif C == "D-":
        grade += int(B)*0.7
    elif C == "F":
        grade += 0
aver=grade/g_sum
if int(1000*aver)%10==5:
    aver=round(int(1000 * aver)+1,-1)/1000
elif int(1000*aver)%100==0:
    aver="%0.2f"%aver
else:
    aver=round(int(1000*aver),-1)/1000
print(aver)