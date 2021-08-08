n = int (input())
a = list (map(int,input().split()))
total = 0

for i in range (len(a)):
    cnt = 0
    for l in reversed (range (0, i)):   #指定した場所から左側を探す
        if a[l] >= a[i]:
            cnt += 1
        else:
            break
    for r in range (i, n):      #指定した場所から右側を探す
        if a[r] >= a[i]:
            cnt += 1
        else:
            break
    cnt = cnt * a[i]
    if total < cnt:
        total = cnt
print (total)