from collections import deque 
s = str (input())
s = list (s)
t = deque()
cnt = 0
for i in range (len(s)):
    if len(t) != 0:
        if s[i] == 'R' and len(t) > 1:
            cnt += 1
        if s[i] == t[-1]:
            if cnt % 2 == 0:
                t.pop()
            else:
                t.popleft()
        if s[i] != t[-1]:
            if cnt % 2 == 0:
                t.append(s[i])
            else:
                t.appendleft(s[i])
    else:
        if s[i] == 'R':
            continue
        else:
            t.append (s[i])
print (t)