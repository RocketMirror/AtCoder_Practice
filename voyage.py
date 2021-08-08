from collections import deque
n, m = map (int, input().split())
l = [[] for _ in range (n)]
counter = [0 for _ in range (n)]
visited = [False] * n
visited[0] = True
for _ in range (m):
    a, b = map (int, input().split())
    a, b = a - 1, b - 1
    l[a].append(b)
    l[b].append(a)
que = deque()
que.append(0)
while que:
    now = que.popleft()
    for i in l[now]:
        if visited[i] == False:
            counter[i] += 1 + counter[now]
            visited[i] = True
            que.append(i)

if counter[n - 1] <= 2 and counter[n - 1] != 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
