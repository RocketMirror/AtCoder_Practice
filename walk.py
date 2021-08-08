x, k, d = map (int, input().split())

if abs(x) - k * d >= 0:
    print (abs(x) - k * d)
    exit()

over = abs(x) % d
under = abs(over - d)
cnt = k - abs(x) // d

if cnt % 2 == 0:
    print (over)
else:
    print (under)