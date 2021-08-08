n, m = map (int, input().split())
h = list (map (int, input().split()))
good = set(range (1, n + 1))
bad = set()
for i in range (m):
    a, b = map (int, input().split())
    if h[a-1] > h[b-1]:
        bad.add(b)
        if b in good:
            good.remove(b)
        if a not in bad:
            good.add(a)
    elif h[a-1] < h[b-1]:
        bad.add(a)
        if a in good:
            good.remove(a)
        if b not in bad:
            good.add(b)
    else:
        bad.add(a)
        bad.add(b)
        if a in good:
            good.remove(a)
        if b in good:
            good.remove(b)
print (len (good))
