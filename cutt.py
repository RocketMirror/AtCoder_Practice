n = int (input())
s = str (input())
ans = 0
for i in range (n - 1):
    cnt = 0
    form = set(s[:i + 1])
    latt = set(s[i + 1:])
    for l in latt:
        if l in form:
            cnt += 1
    if cnt >= ans:
        ans = cnt
print (ans)
