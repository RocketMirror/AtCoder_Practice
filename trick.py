n, k = map (int, input().split())
l = [True] * n
for _ in range (k):
    d = int (input()) 
    a = list (map (int, input().split()))
    for i in a:
        l[i - 1] = False
cnt = 0
for e in l:
    if e:
        cnt += 1
print (cnt)