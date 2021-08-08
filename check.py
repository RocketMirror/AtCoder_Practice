n, m = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range (n)]
cd = [list(map(int,input().split())) for _ in range (m)]

for i in ab:
    dist = 10**9
    for j in range (m):
        d = abs(i[0] - cd[j][0]) + abs(i[1] - cd[j][1])

        if d < dist:
            dist = d
            ind = j + 1
    print(ind)
