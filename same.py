a, b, c = map (int,input().split())
l = [a, b, c]
big = max (l)
l.remove (big)
cnt = 0

for i in range (51):
    if l[0] == big:
        small = l[1]
        break
    if l[1] == big:
        small = l[0]
        break

    l[0] += 1
    l[1] += 1
    cnt += 1

if (big - small) % 2 == 0:
    cnt += (big - small) // 2
    print (cnt)
else:
    cnt += (big - small + 1) // 2 + 1
    print (cnt)
