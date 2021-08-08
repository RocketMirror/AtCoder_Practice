import itertools
h, w, k = map (int, input().split())
l = []
for i in range (h):
    c = str (input())
    l.append (c)
t, f = 1, 0
check = [[f, t]] * (h + w)
pro = list (itertools.product (*check))

cnt = 0
ll = tuple (l)
for p in pro:
    l = list (ll)
    for q in range (h + w):
        if p[q] == t:
            if q < h:
                l[q] = '.' * w
            else:
                for o in range (h):
                    l[o] = l[o][:q-h] + '.' + l[o][q-h+1:]
                    l[o] = l[o][:w]
    s = ''.join (l)
    # print (p)
    # print (s)
    if s.count ('#') == k:
        cnt += 1
print (cnt)

