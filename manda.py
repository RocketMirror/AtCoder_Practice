n = int (input())
a = list (map(int,input().split()))
big = 0

for i in range (n):
    total = a[i]
    for j in range (i, n):
        total = min (total, a[j])
        ans = total * (j - i + 1)
        if big < ans:
            big = ans
print (big)
