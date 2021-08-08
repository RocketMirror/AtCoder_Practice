n = int (input())
A = sorted ((map (int, input().split())), reverse= True)
l = []
t = 10000000000
cnt = 0
for a in A:
    if a == t:
        cnt += 1
    else:
        t = a
        cnt = 1
    if cnt == 2:
        l.append (a)
    if cnt == 4:
        print (a ** 2)
        exit()
    if len (l) == 2:
        print (l[0] * l[1])
        exit()
print (0)

