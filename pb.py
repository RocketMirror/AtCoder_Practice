s = input()
l = [0] * 2
ll = []
cnt = 0

for i in range (len(s)):
    if s[i] == 'A':
        l[0] += 1
    if s[i] == 'Z':
        if l[0] ==1:
            l[1] += 1
    if l[0] > 1:
        l[0] = 1
    if l[1] > 1:
        l[1] = 1
    if l[0] - l[1] == 1:
        cnt += 1
    if l[0] - l[1] == 0:
        ll.append(cnt)
        cnt = 0

print (max(ll) + 1)

