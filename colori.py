from collections import deque
n = int(input())
inp = []
connect = [[] for _ in range (n)]
for _ in range (n - 1):
    a, b = map (int, input().split())
    a, b = a - 1, b - 1
    connect[a].append(b)
    inp.append(b)

que = deque([0])
color = [-1] * n

while que:
    now = que.popleft()
    c = 0
    for new in connect[now]:
        if c == color[now]:
            c += 1
        color[new] = c
        c += 1
        que.append(new)
print (max(color) + 1)
for i in inp:
    print(color[i] + 1)

