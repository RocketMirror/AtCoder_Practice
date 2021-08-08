n, m = map (int,input().split())
ll = [0] * n

for i in range (m):
    a, b = map (int,input().split())
    ll[a - 1] += 1
    ll[b - 1] += 1

for j in range (n):
    print (ll[j])


