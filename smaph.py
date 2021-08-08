n, m, t = map (int, input().split())
juden = 0
bb = 0
nokori = n
shinnokori = n

for i in range (m):
    a, b = map (int, input().split())
    shouhi = a - bb

    if nokori - shouhi <= 0:
        print ('No')
        exit()
    juden = b - a
    nokori - shouhi + juden
    shinnokori = nokori - shouhi + juden
    # print(nokori)
    # print(shouhi)
    # print(juden)
    # print (shinnokori)
    if shinnokori > n:
        shinnokori = n
    nokori = shinnokori

    bb = b
# print (t - b)
# print (nokori)
# print (shinnokori)

if nokori <= t - b:
    print ('No')

else:
    print('Yes')
