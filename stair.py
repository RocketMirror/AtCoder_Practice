n, m = map (int, input().split())
s = set (int(input()) for _ in range (m))
dp = [0] * (n + 1)
dp[0] = 1
if 1 in s:
    dp[1] = 0
else:
    dp[1] = 1

if n == 1:
    print (dp[1])
    exit()

for i in range (2, n + 1):
    if i in s:
        continue
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
        if dp[i] == 0:
            print (0)
            exit()
print (dp[i] % 1000000007)
