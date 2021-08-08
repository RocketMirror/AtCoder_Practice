h, w = map (int, input().split())
l = [[0 for _ in range (w + 2)] for _ in range (h + 2)]
s = [input() for _ in range (h)]

def mine(i, j):
    if l[i][j] == '#':
        return '#'
    else:
        return l[i][j] + 1

for i in range (h):
    for j in range (w):
        if s[i][j] == '#':
            l[i][j] = mine(i, j)
            l[i][j + 1] = mine(i, j + 1)
            l[i][j + 2] = mine(i, j + 2)
            l[i + 2][j] = mine(i + 2, j)
            l[i + 2][j + 1] = mine(i + 2, j + 1)
            l[i + 2][j + 2] = mine(i + 2, j + 2)
            l[i + 1][j] = mine(i + 1, j)
            l[i + 1][j + 2] = mine(i + 1, j + 2)
            l[i + 1][j + 1] = '#'
for i in range (1, h + 1):
    ans = list(map(str, (l[i][1 : w + 1])))
    print (''.join(ans))

