n = int(input())
a = list (map (int, input().split()))
l = []
for i in range (n):
    l.append ([a[i], i])
a.sort()
b, c = a[n // 2 - 1], a[n // 2]
l = sorted (l)
a_ = []
for j in range (n):
    a_.append (l[j][1])
check = set(a_[:n // 2])

for i in range (n):
    if i in check:
        print(c)
    else:
        print(b)