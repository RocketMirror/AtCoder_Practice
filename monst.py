import math
n = int (input())
a = list (map (int, input().split()))
gcd = math.gcd (a[0], a[1])
if len(a) > 2:
    for i in range (2, n):
        gcd = math.gcd (gcd, a[i])
print (gcd)
    
    