a, b = map (int, input().split())
height = 0

for i in range (1, 1000):
    if b - a == i:
        for j in range(1, i + 1):
            height += j
        print (height - b)
        exit()

