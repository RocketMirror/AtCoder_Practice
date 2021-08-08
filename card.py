n = int (input())
dic = {}
for _ in range (n):
    s = str (input())
    if s in dic.keys():
        dic[s] += 1
    else:
        dic[s] = 1

m = int (input())
for _ in range (m):
    t = str (input())
    if t in dic.keys():
        dic[t] -= 1
    else:
        dic[t] = -1
dic = sorted (dic.values(), reverse= True)
if dic[0] < 0:
    print (0)
else:
    print (dic[0])
