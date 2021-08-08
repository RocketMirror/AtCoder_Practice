n = int (input())
s = set()
for i in range (n):
    w = str (input())
    if w in s:
        print ('No')
        exit()
    if i == 0:
        bottom = w[-1]
        s.add (w)
        continue
    if w[0] != bottom:
        print ('No')
        exit()
    bottom = w[-1]
    s.add (w)
print ('Yes')