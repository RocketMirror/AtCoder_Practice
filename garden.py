n = int (input())
h = list (map (int, input().split()))
cnt = 0
ans = 0
for i in range (100):
    f = False
    for j in range (n):
        if h[j] == 0:
            if f:
                cnt += 1
                f = f == False
            else:
                continue
        else:
            h[j] = h[j] - 1
            if f:
                continue
            else:
                f = f == False
    if f:
        cnt += 1
    if sum(h) == 0:
        break
print (cnt)