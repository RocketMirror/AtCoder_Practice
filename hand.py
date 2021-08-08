n = int(input())
l = [[0 for _ in range (10)] for _ in range (10)]
for i in range (1, n + 1):
    l[int((str(i))[0])][int((str(i))[-1])] += 1
cnt = 0
for j in range (1, 10):
    for k in range (1,10):
        cnt += l[j][k] * l[k][j]
print(cnt)