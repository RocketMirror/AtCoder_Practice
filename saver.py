n = int (input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range (n):
    if a[i] >= b[i]:
        cnt += b[i]
    else:
        amari = b[i] - a[i]
        cnt += a[i]
        if a[i + 1] >= amari:
            cnt += amari
        else:
            cnt += a[i + 1]
        if a[i + 1] - amari < 0:
            a[i + 1] = 0
        else:
            a[i + 1] = a[i + 1] - amari
print (cnt)

