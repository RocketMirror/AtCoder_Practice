from functools import reduce
import math
def mygcd(*diffs):
    return reduce(math.gcd, diffs)
ans = 0
k = int(input())
for a in range (1, k + 1):
    for b in range (1, k + 1):
        for c in range (1, k + 1):
            l = [a, b, c]
            ans += mygcd(*l)
print (ans)
