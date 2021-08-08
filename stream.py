n, m = map (int, input().split())
x = sorted (list (map (int, input().split())))
l = sorted ([x[i + 1] - x[i] for i in range (m - 1)])
for j in range (n - 1):
    if l == []:
        break
    del l[-1]
print (sum(l))
