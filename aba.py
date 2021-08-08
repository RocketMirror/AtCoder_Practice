import math
a, b, k = map(int,input().split())
aa, bb = a, b
total = math.factorial(a + b) // (math.factorial(a) * math.factorial(b))
A = math.factorial(a - 1 + b) // (math.factorial(a - 1) * math.factorial(b))
B = A + math.factorial(a + b - 1) // (math.factorial(a) * math.factorial(b - 1))
ans = ''
acnt = 0
bcnt = 0
while A != k and B != k:
    if k < A:
        ans += 'a'
        a -= 1
        acnt += 1
    elif k < B:
        ans += 'b'
        b -= 1
        bcnt += 1
        k -= A
    A = math.factorial(a - 1 + b) // (math.factorial(a - 1) * math.factorial(b))
    B = A + math.factorial(a + b - 1) // (math.factorial(a) * math.factorial(b - 1))
if A == k:
    ans += 'a'
    acnt += 1
elif B == k:
    ans += 'b'
    bcnt += 1
ans += 'b' * (bb - bcnt) + 'a' * (aa - acnt)
print(ans)
