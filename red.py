s = int (input())
l = [1, 0, 0]
for i in range (3, s + 1):
    l.append (l[i - 3] + l[i - 1])
print (l[s] % (1000000000 + 7))