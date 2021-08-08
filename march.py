from itertools import combinations
n = int(input())
mcnt, acnt, rcnt, ccnt, hcnt = 0, 0, 0, 0, 0
for _ in range (n):
    s = input()
    if s[0] == 'M':
        mcnt += 1
    if s[0] == 'A':
        acnt += 1
    if s[0] == 'R':
        rcnt += 1
    if s[0] == 'C':
        ccnt += 1
    if s[0] == 'H':
        hcnt += 1
com = combinations((mcnt,acnt,rcnt,ccnt,hcnt),3)
ans = 0
for co in com:
    cnt = 1
    for c in co:
        cnt *= c
    ans += cnt
print(ans)