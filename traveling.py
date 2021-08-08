n = int (input())
t = [0]
x = [0]
y = [0]

for i in range (n):
    txy = list (map (int, input().split()))
    t.append (txy[0])
    x.append (txy[1])
    y.append (txy[2])

for j in range (1, n + 1):
    dis = abs (x[j] - x[j - 1]) + abs (y[j] - y[j - 1])
    time = t[j] - t[j - 1]
    if dis > time or (time - dis) % 2 != 0:
        print ('No')
        exit()

print ('Yes')