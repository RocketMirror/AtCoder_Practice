import itertools
import copy
h, w, k = map (int, input().split())
yoko = []
tate = []
for i in range (h):
    c = str (input())
    c = list (c)
    yoko.append (c)

for j in range (w):
    r = ''
    for y in range (h):
        r += yoko[y][j]
        r = list (r)
    tate.append (r)

l = yoko + tate
lll = copy.copy(l)

com = itertools.combinations (list(range(h + w)), k)
cnt = 0
for s in range (1, h + w):
    com = itertools.combinations (list(range(h + w)), s)
    for o in com:
        for p in o:
            if p < h:
                l[p] = ['.'] * w
                for q in range (h, h + w):
                    l[q][p] = '.'
            else:
                l[p] = ['.'] * h
                for s in range (0, h):
                    l[s][p - h] = '.'
        ll = [flatten for inner in l for flatten in inner]
        print (ll)
        if ll.count('#') // 2 == k:
            cnt += 1
        l = lll
    print (cnt)