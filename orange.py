a, b, w = map (int, input().split())
w = w * 1000

for i in range (1, 1000001):
    if a * i <= w and w <= b * i:
        anss = i
        break
else:
    print('UNSATISFIABLE')
    exit()        

for j in range (1000001, 0, -1):
    if a * j <= w and w <= b * j:
        ansl = j
        break

print (i, j)

