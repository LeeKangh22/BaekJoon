phone=input()
answer=0
for i in range(0,len(phone)):
    if phone[i]=='A' or phone[i]=='B' or phone[i]=='C':
        answer+=3
    if phone[i]=='D' or phone[i]=='E' or phone[i]=='F':
        answer+=4
    if phone[i]=='G' or phone[i]=='H' or phone[i]=='I':
        answer+=5
    if phone[i]=='J' or phone[i]=='K' or phone[i]=='L':
        answer+=6
    if phone[i]=='M' or phone[i]=='N' or phone[i]=='O':
        answer+=7
    if phone[i]=='P' or phone[i]=='Q' or phone[i]=='R' or phone[i]=='S':
        answer+=8
    if phone[i]=='T' or phone[i]=='U' or phone[i]=='V':
        answer+=9
    if phone[i]=='W' or phone[i]=='X' or phone[i]=='Y' or phone[i]=='Z':
        answer+=10
print(answer)