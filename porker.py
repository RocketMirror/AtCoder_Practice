import copy
k = int (input())
s = str (input())
t = str (input())
total = (9 * k - 8) * (9 * k - 9)
dic = {1:k, 2:k, 3:k, 4:k, 5:k, 6:k, 7:k, 8:k, 9:k}
dic_s = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
dic_t = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for i in range (4):
    dic[int (s[i])] -= 1
    dic[int (t[i])] -= 1
    dic_s[int (s[i])] += 1
    dic_t[int (t[i])] += 1

ss = copy.deepcopy(dic_s)
tt = copy.deepcopy(dic_t)
d = copy.deepcopy(dic)

sscore = 0
tscore = 0
cnt = 0

for j in range (1, 10):
    dic_s = copy.deepcopy(ss)
    dic = copy.deepcopy(d)
    if dic[j] == 0:
        continue
    dic_s[j] += 1
    dic[j] -= 1
    dicc = copy.deepcopy(dic)
    for k in range (1, 10):
        dic_t = copy.deepcopy(tt)
        dic = copy.deepcopy(dicc)
        sscore = 0
        tscore = 0
        if dic[k] == 0:
            continue
        dic_t[k] += 1
        dic[k] -= 1
        for l in range (1, 10):
            sscore += l * 10 ** dic_s[l]
            tscore += l * 10 ** dic_t[l] 
        
        if sscore > tscore:
            if j == k:
                cnt += (dic[j] + 2) * (dic[j] + 1) 
            else:
                cnt += (dic[j] + 1) * (dic[k] + 1)

print (cnt / total)
        


