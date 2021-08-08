import math
n, X = map (int, input().split())
x = list (map (int, input().split()))
x.append (X)
x = sorted (x)
l = []
for i in range (n):
    l.append (x[i + 1] - x[i])
ans = l[0]
if len (l) == 1:
    print (ans)
    exit()
for j in range (1, len(l)):
    ans = math.gcd (ans, l[j])
print (ans)