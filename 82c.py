n = int(input())
a = list(map(int,input().split()))
cnt = [0] * (10**9+1)
ans = 0
for i in a:
    cnt[i] += 1
    if cnt[i] < i:
        ans += 1
    if cnt[i] == i:
        ans -= i - 1
    if cnt[i] > i:
        ans += 1
print(ans)
exit()
    