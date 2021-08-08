n, m = map (int, input().split())
ac = [0] * n
wa = [0] * n
w_cnt = 0
for i in range (m):
    p, s = map (str, input().split())
    p = int (p) - 1
    if ac[p] > 0:
        continue
    else:
        if s == 'AC':
            ac[p] += 1
            w_cnt += wa[p]
        else:
            wa[p] += 1
print (sum(ac), w_cnt)