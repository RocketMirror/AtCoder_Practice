import math
n = int (input())
a = list (map (int, input().split()))
b = [i % 200 for i in a]
b = sorted (b)

l = [b[0]]
ll = []
cnt = 1
for j in range (1, len (b)):
    if b[j] == l[-1]:
        cnt += 1
    else:
        ll.append (cnt)
        l.append (b[j])
        cnt = 1
    
ll.append (cnt)

lll = [e * (e - 1) // 2 for e in ll]
print (sum(lll))
    