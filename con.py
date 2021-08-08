s = input()
k = int (input())
p = 0
for v in s:
    if v == s[0]:
        p += 1
    if p == len(s):
        print (len(s) * k // 2)
        exit()

l = []
cnt = 1
a = s[0]
c = 1
for i in range (1, len(s)):
    if s[i] == a:
        cnt += 1
    else:
        cnt = 1
        a = s[i]
    if cnt == 2:
        l.append(1)
        cnt = 0
        a = ''

for j in range (1, len(s)):
    if s[j] == s[0]:
        c += 1
    else:
        break
if s[0] == s[-1] and c % 2 != 0 and cnt % 2 != 0:
    print (sum(l) * k + (k - 1))
    exit()


print (sum(l) * k)
