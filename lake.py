k, n = map (int, input().split())
a = list (map(int, input().split()))
long = a[0] + k - a[-1]
for i in range (n - 1):
    long = max (long, a[i + 1] - a[i])
print (k - long)
