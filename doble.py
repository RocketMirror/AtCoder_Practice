from collections import deque
n, m = map (int, input().split())
counter = [0] * (m + 2)
connect = [[] for _ in range (m + 2)]
que = deque()
for _ in range (m):
    a, b = map (int, input().split())
    connect[a].append (b)
    connect[b].append (a)

que.append (1)
visited = [False] * (m + 2)
visited[1] = True

while que:
    now = que.popleft()
    for i in connect[now]:
        if visited[i] == False:
            counter[i] = now
            visited[i] = True
            que.append(i)
counter = filter (lambda e: e != 0, counter)
print ('Yes')
for j in counter:
    print (j)
