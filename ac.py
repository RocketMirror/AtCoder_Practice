n, q = map (int, input().split())
lis = [0] * (n + 1)
s = str (input())
copy = s.replace ('AC', '01')
for j in range (1, n + 1):
    if copy[j] == '1':
        lis[j] = lis[j - 1] + 1
    else:
        lis[j] = lis[j - 1]
for i in range (q):
    l, r = map (int, input().split())
    print (lis[r] - lis[l])
    