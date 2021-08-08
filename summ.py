n = int (input())
a = list (map (int, input().split()))
ans = 0
ca = [0]
for i in range(0, n):
    ca.append(ca[i] + a[i])

for j in range (n):
    ans += a[j] * (ca[n] - ca[j + 1])

print (ans % (10 ** 9 + 7))