n, k = map (int, input().split())
ans = 0
for i in range (1, n + 1):
    bor = i
    for j in range (10000):
        if bor >= k:
            pro = 0.5 ** j / n
            ans += pro
            break
        else:
            bor *= 2
print (ans)