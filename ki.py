from collections import deque
n, q = map (int, input().split())
connect = [[] for _ in range (n + 1)]
counter = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
que = deque()
que.append(1)
for _ in range (n - 1):
    a, b = map (int, input().split())
    connect[a].append(b)
    connect[b].append(a)

for _ in range (q):
    p, x = map (int, input().split())
    counter[p] += x

while que:
    now = que.popleft()
    for i in connect[now]:
        if visited[i] == False:
            counter[i] += counter[now]
            visited[i] = True
            que.append(i)
print (*counter[1:])

