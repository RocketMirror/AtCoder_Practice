n = int (input())
goukei = 0

for j in range (n):
    a, b = map (int, input().split())
    if (a + b) % 2 == 0:
        goukei += (a + b) // 2 * (b - a + 1)
    else:
        goukei += (a + b) * ((b - a + 1) // 2)

print (goukei)