n = int (input())
a = list (map (int, input().split()))
l = [0]
ans = 0
for i in a:
    if i < l[-1]:
        l.append (l[-1])
        ans += l[-1] - i
    else:
        l.append (i)
print (ans)
    
