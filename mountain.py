n = int (input())
l = []
for _ in range (n):
    st = list (map (str, input().split()))
    st[1] = int(st[1])
    l.append(st)
l = sorted (l, key= lambda x: x[1])
print (l[-2][0])
