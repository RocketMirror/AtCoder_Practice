from itertools import accumulate
import bisect
n, m, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
aacc = [0] + list(accumulate(a))
bacc = list(accumulate(b))
ans = 0
for i in range (n + 1):
    bcnt = k  - aacc[i]
    if bcnt < 0:
        break
    bn = bisect.bisect_right(bacc, bcnt)
    ans = max(ans,i + bn)
print(ans)
