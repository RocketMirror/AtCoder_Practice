h, w = map (int, input().split())
l = ['.' + input() + '.' for _ in range (h)]
ll = ['.' * (w + 2)] + l + ['.' * (w + 2)]
di = (-1,0,1,0)
dj = (0,-1,0,1)
for i in range (1, h + 1):
    for j in range (1, w + 1):
        if ll[i][j] == '#':
            for k in range (4):
                if ll[i + di[k]][j + dj[k]] == '#':
                    break
            else:
                print('No')
                exit()
print('Yes')