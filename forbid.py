x, n = map (int, input().split())
p = list (map (int, input().split()))
l = [0] * 2000
plus = 0
minus = 0
for i in p:
    l[i] += 1
if l[x] == 0:
    print (x)
else:
    for j in range (1, 1000):
        if l[x + j] != 0:
            plus += 1
        else:
            plus += 1
            break
    for k in range (1, 1000):
        if l[x - k] != 0:
            minus += 1
        else:
            minus += 1
            minus *= -1
            break
    if plus + minus >= 0:
        ans = minus
    else:
        ans = plus
    print (x + ans)