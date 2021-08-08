import math
mod = 10 ** 9 + 7
n, a, b = map (int, input().split())
#繰り返し二乗法
def pow (x, n, mod):
    ans = 1
    while n > 0:
        if n % 2 != 0:
            ans *= x % mod
        x = x * x % mod
        n = n // 2
    return ans
    
#nCk　フェルマーの小定理
def nck (n, k, mod):
    p, q = 1, 1
    for i in range (k):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod

print ((pow(2, n, mod) - 1 - nck(n, a, mod) - nck(n, b, mod)) % (10 ** 9 + 7))
