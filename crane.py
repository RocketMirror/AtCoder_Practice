x, y = map (int, input().split())
for i in range (x + 1):
    j = x - i
    if 2 * i + 4 * j == y:
        print ('Yes')
        exit()
print ('No')