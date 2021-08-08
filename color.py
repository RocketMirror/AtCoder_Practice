n = int (input())
a = list (map (int, input().split()))
l = [0] * 8
cnt = 0
cnt_high = 0
for i in a:
    if 1 <= i and i <= 399:
        l[0] += 1
    elif 400 <= i and i <= 799:
        l[1] += 1
    elif 800 <= i and i <= 1199:
        l[2] += 1
    elif 1200 <= i and i <= 1599:
        l[3] += 1
    elif 1600 <= i and i <= 1999:
        l[4] += 1
    elif 2000 <= i and i <= 2399:
        l[5] += 1
    elif 2400 <= i and i <= 2799:
        l[6] += 1
    elif 2800 <= i and i <= 3199:
        l[7] += 1
    else:
        cnt += 1

ans = list (filter (lambda e: e != 0, l))
cnt_low = len(ans)
cnt_high = len(ans) + cnt
if len(ans) == 0:
    cnt_low = 1

print (cnt_low, cnt_high)