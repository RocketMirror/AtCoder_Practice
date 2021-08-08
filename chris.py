n, k = map (int, input().split())
l = [int(input()) for _ in range (n)]
down = sorted (l)
ans = 10**50
for i in range (n - k + 1):
    cnt = (abs(down[i] - down[i + k - 1]))
    ans = min (ans, cnt)
print(ans)