import itertools
n, d = map (int, input().split())
l = [list (map (int, input().split())) for _ in range (n)]
com = list (itertools.combinations (l, 2))
cnt = 0
for c in com:
    dis = 0
    for j in range (d):
        dis += (c[0][j] - c[1][j]) ** 2
    dis = dis ** 0.5
    if dis == int (dis):
        cnt += 1 
print (cnt)