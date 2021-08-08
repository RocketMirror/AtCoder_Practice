import math

n = int (input())
N = int (math.sqrt(n) + 1)
s = set()

for j in range (2, 35):
    for i in range (2, N):
        if i ** j > n:
            break
        if i ** j <= n:
            s.add(i ** j)
                
print (n - len (s))