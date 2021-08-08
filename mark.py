n, k = map (int, input().split())
a = list (map (int, input().split()))
l = []
b = a[0]
for j in range (k, n):
    o = a[j]
    b = a[j - k]
    if o > b:
        print('Yes')
        b = a[j - k]
    else:
        print ('No')
        b = a[j - k]
    