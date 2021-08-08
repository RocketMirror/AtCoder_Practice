n, time = map (int, input().split())
t = list (map (int, input().split()))
cnt = 0

for i in range (1, n):
    if t[i] - t[i - 1] <= time:
        cnt += t[i] - t[i - 1]
    else:
        cnt += time

print (cnt + time)