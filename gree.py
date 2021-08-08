import math
n = int (input())
dic = {}
for i in range (n):
    s = sorted (input())
    s = ''.join (s)
    if s in dic.keys():
        dic[s] += 1
    else:
        dic[s] = 1
num = dic.values()
ans = [(i * (i - 1)) // 2 for i in num]
print (sum(ans))