from collections import deque
r, c = map (int, input().split())
sy, sx = map (int, input().split())
gy, gx = map (int, input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1
grid = [input() for _ in range (r)]
que = deque()
que.append((sy, sx))
dist = [[-1 for _ in range(c)] for _ in range (r)]
dist[sy][sx] = 0

dy = (0, 1, 0, -1)
dx = (1, 0, -1 ,0)

while que:
    now = que.popleft()
    y, x = now

    for di in range (4):
        ny = y + dy[di]
        nx = x + dx[di]

        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        if grid[ny][nx] == '#':
            continue
        if dist[ny][nx] != -1:
            continue

        dist[ny][nx] = dist[y][x] + 1
        que.append((ny, nx))

print (dist[gy][gx])

