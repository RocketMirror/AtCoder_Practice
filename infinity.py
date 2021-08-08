s = str (input())
k = int (input())
cnt = 0
for i in range (len(s)):
    if s[i] == '1':
        cnt += 1
        continue
    else:
        ans = s[i]
        break
    if cnt == len (s):
        print (1)
        exit()
if k - 1 < i:
    print (1)
else:
    print (s[i])
