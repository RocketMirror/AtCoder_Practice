from collections import deque
S = str (input())
t = deque()
f = False
for s in S:
    if len (t) == 0:
        if s == 'R':
            continue
        else:
            t.append(s)
    else:
        if s == 'R':
            f = f == False
        elif f:
            if t[0] == s:
                t.popleft()
            else:
                t.appendleft(s)
        else:
            if t[-1] == s:
                t.pop()
            else:
                t.append(s)
if f:
    t = reversed (t)
print (*t, sep= '')

