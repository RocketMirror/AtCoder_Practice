h, w = map (int, input().split())
l = []
for _ in range (h):
    s = input()
    if s == '.' * w:
        continue
    else:
        l.append(list(s))
ind = []
for i in range (w):
    for j in l:
        if j[i] == '#':
            break
    else:
        ind.append(i)
for o in l:
    for p in reversed(ind):
        del o[p]
for q in l:
    print(''.join(q))