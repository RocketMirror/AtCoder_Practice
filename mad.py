import itertools
n = int (input())
A = []
B = []
C = []
D = []
E = []
for i in range (n):
    a, b, c, d, e = map (int, input().split())
    A.append (a)
    B.append (b)
    C.append (c)
    D.append (d)
    E.append (e)

l = list (range (n))

com = itertools.combinations (l, 3)

ans = 0
for c in com:
    x = min (max (A[c[0]], A[c[1]], A[c[2]]), max (B[c[0]], B[c[1]], B[c[2]]), max (C[c[0]], C[c[1]], C[c[2]]), max (D[c[0]], D[c[1]], D[c[2]]), max (E[c[0]], E[c[1]], E[c[2]]))
    if x > ans:
        ans = x
print (ans)