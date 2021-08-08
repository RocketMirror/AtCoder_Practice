n = int (input())
S = []
t = set()
for i in range (n):
    sp = list(map (str, input().split())) +[i + 1]
    S.append(sp)
    t.add(sp[0])
l = sorted (S)

t = sorted (list (t))
ll = []
for o in range (len(t)):
    ll.append([])
    
for j in range (len(t)):
    for k in range (n):
        if t[j] == l[k][0]:
            l[k][1] = int (l[k][1])
            ll[j].append (l[k][1:3])
        else:
            continue

for p in range (len(t)):
    ll[p] = sorted (ll[p],key= lambda x: x[0])
    ll[p].reverse()

for q in range (len (t)):
    for r in range (len(ll[q])):
        print (ll[q][r][1])