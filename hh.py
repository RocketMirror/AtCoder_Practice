import itertools
import copy
h, w, k = map (int, input().split())
yoko = []
for i in range (h):
    c = list (input())
    yoko.append (c)

l = [[0, 1]] * (h + w)

pro = itertools.product (*l) 

cnt = 0
for o in pro:
    yoko_copy = copy.copy(yoko)
    for p in range (h + w):
        if p < h:
            if o[p] == 1:
                yoko_copy[p] = ['.'] * w
        else:
            if o[p] == 1:
                for q in yoko_copy:
                    q[p - h] = '.'
    yoko_count = [flatten for inner in yoko_copy for flatten in inner]
    print (yoko_copy)
    if yoko_count.count ('#') == k:
        cnt += 1
print (cnt)