n = int (input())
d = {}
for _ in range (n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
d_sort = sorted (d.items(), key= lambda x: x[1], reverse= True)

l = []
high = d_sort[0][1]
l.append(d_sort[0][0])
for j in range (1, len(d)):
    if high == d_sort[j][1]:
        l.append(d_sort[j][0])
        high = d_sort[j][1]
    else:
        break
l.sort()
for ans in l:
    print (ans)




