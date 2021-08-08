n = int(input())
l = [int(input()) - 1 for _ in range (n)]
akari = 0
cnt = 0
while akari != 1:
    akari = l[akari]
    cnt += 1
    if cnt > n:
        print (-1)
        exit()
print (cnt)

