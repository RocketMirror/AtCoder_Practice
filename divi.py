n = int (input())
a = sorted(list (map (int, input().split())))
large = a[-1]
dic = {}
t = 'x'
for aa in a:
    if aa == t:
        dic[t] += 1
    else:
        dic[aa] = 1
    t = aa

s = set()
l = []
for e in a:
    if e not in s:
        l.append (e)
        for j in range (e, large + 1, e):
            s.add (j)
   
cnt = 0
for i in range (len (l)):
    if dic[l[i]] >= 2:
        continue
    else:
        cnt += 1
print (cnt)