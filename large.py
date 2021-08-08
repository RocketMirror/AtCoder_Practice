n, k = map (int, input().split())
l = [0]
for e in range (n + 1):
    l.append (l[-1] + e)
ans = 0
for i in range (k, n + 2):
    up = l[-1] - l[n - i + 1]
    down = l[i]
    ans += (up - down + 1) % (1000000000 + 7)
    
print (ans % (1000000000 + 7))