from collections import deque
h, w = map (int, input().split())
s = [input() for _ in range (h)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
ans = -1
for i in range (h):
    for j in range (w):
        if s[i][j] == '#': continue
        que = deque()
        counter = [[0 for _ in range (w)] for _ in range (h)]
        visited = [[False for _ in range (w)] for _ in range (h)]
        sy, sx = i, j
        que.append ((sy, sx))
        visited[i][j] = True
        while que:
            now = que.popleft()
            y, x = now
            for k in range (4):
                ny = y + dy[k]
                nx = x + dx[k]
                if ny < 0 or nx < 0 or ny > h - 1 or nx > w - 1:
                    continue
                if visited[ny][nx]:
                    continue
                if s[ny][nx] == '#':
                    continue

                counter[ny][nx] += counter[y][x] + 1
                visited[ny][nx] = True
                que.append((ny, nx))
        counter = [flatten for inner in counter for flatten in inner]
        ans = max(max(counter), ans)
print(ans)