import itertools
import math
n = int (input())
l = []
for j in range (1, n + 1):
    l.append (str(j))

com = map (''.join, (itertools.permutations(l)))
com = sorted (list (map (int, com)))

p = list (map(str,input().split()))
q = list (map(str,input().split()))

p =  int(''.join (p))
q =  int(''.join (q))

for i in range (len(com)):
    if com[i] == p:
        a = i + 1
    if com[i] == q:
        b = i + 1

print (abs (a - b))