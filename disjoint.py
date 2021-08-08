from fractions import gcd
a, b = map(int,(input().split()))
g = gcd(a, b)
o = g

cnt = 0
i = 2
while i <= g**0.5 + 1:
    if o < i:
        break
    if o % i == 0:
        cnt += 1
        while o % i == 0:
            o //= i
    i += 1
if o != 1:
    cnt += 1

print(cnt + 1)
    
