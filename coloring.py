from collections import deque
n = int(input())
inp = []
connect = [[] for _ in range (n)]
con_num = []
for _ in range (n - 1):
    a, b = map (int, input().split())
    a, b = a - 1, b - 1
    connect[a].append(b)
    connect[b].append(a)
    inp.append((a, b))
variation = 0
for i in connect:
    con_num.append(len(i))
    variation = max (variation, len(i))
stock = [deque(range (variation)) for _ in range (n)]
print (variation)
for j in inp:
    if con_num[j[0]] >= con_num[j[1]]:
        st = stock[j[0]].popleft()
        print (st + 1)
        try:
            stock[j[1]].remove(st)
        except ValueError:
            pass
    else:
        st = stock[j[1]].popleft()
        print (st + 1)
        try:
            stock[j[0]].remove(st)
        except ValueError:
            pass

        



