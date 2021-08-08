n, k = map(int,input().split())
s = input()
total = []
memo = s[0]
if memo == 'L':
    rcnt = 0
    lcnt = 1
else:
    lcnt = 0
    rcnt = 1
for i in range (1, n):
    if s[i] == memo:
        if s[i] == 'L':
            lcnt += 1
        else:
            rcnt += 1
    else:
        if s[i] == 'L':
            total.append(rcnt)
            lcnt = 1
            rcnt = 0
        else:
            total.append(lcnt)
            rcnt = 1
            lcnt = 0
    memo = s[i]
total.append(rcnt if rcnt != 0 else lcnt)
total = [0] + total + [0]
if k > len(total) // 2:
    k = len(total) // 2
cnt = 0
for i in range (1, len(total)-1):
    if i <= k * 2 + 1:
        cnt += total[i]
    else:
        cnt += total[i] - 1
print(cnt - 1)