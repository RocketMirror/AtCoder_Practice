n = int (input())
l = list (map (int, input().split()))
cnt = 0
for i in range (n - 2):
    for j in range (i, n - 1):
        for k in range (j, n):
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                s = sorted ([l[i], l[j], l[k]])
                if s[2] < s[0] + s[1]:
                    cnt += 1
print (cnt)


