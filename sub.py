s = str (input())
t = str (input())
ans = 10000
for i in range (len(s)-len(t)+1):
    cnt = 0
    for j in range (len(t)):
        if s[i + j] != t[j]:
            cnt += 1
    if ans > cnt:
        ans = cnt
print (ans)