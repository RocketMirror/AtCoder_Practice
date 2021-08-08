import itertools
a, b, c, d = map (int, input().split())
n = [a, b]
m = [c, d]
pro = itertools.product (n, m)
ans = -10000000000000000000
for p in pro:
    e = p[0] * p[1]
    if ans <= e:
        ans = e
print (ans)
