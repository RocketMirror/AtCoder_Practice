import itertools
import math
total = 0
cnt = 0
n, k = map (int, input().split())
l = []
for i in range (n):
    t = list (map (int, input().split()))
    l.append (t)

com = list (itertools.permutations (list (range (1, n))))

if n == 2:
    if l[0][1] + l[1][0] == k:
        print (1)
    else:
        print (0)
    exit()


for j in range (math.factorial(n - 1)):
    total += (l[0][com[j][0]])     #１→？

    for kk in range (n - 2):
        total += l[com[j][kk]][com[j][kk + 1]]

    total += l[com[j][kk + 1]][0]     #最後→１
    if total == k:
        cnt += 1
    total = 0

print (cnt)