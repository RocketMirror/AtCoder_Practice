import itertools
import math

n = int (input())
xl = []
yl = []

for i in range (n):
    x, y = map (int, input().split())
    xl.append (x)
    yl.append (y)

xx = list(itertools.permutations (xl))
yy = list(itertools.permutations (yl))
kyori = 0

for j in range (math.factorial(n)):
    for k in range (n - 1):
        kyori += math.sqrt ((xx[j][k] - xx[j][k + 1]) ** 2 + (yy[j][k] - yy[j][k + 1]) ** 2)

print (kyori / math.factorial(n))