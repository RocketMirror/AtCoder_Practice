import itertools
n = int (input())
a = list (map (int, input().split()))
pro = itertools.product ([0, 1], repeat= n - 1)

ans = 10 ** 20

for bit in pro:
    bit = list(bit) + [1]
    score = 0
    cur = 0
    for i in range (n):
        cur |= a[i]
        if bit[i] == 1:
            score ^= cur
            cur = 0
    ans = min (ans, score)
print (ans)




