n, x, y = map (int, input().split())
l = [0] * (n + 1)
for i in range (1, n):
    for j in range (i + 1, n + 1):
        l[min(j - i, abs(x - i) + abs(y - j) + 1)] += 1
[print(l[k]) for k in range (1, n)]
