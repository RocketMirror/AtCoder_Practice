n = int (input())
s = str (input())
p = ''
e = [0]
w = [0]
for i in range (1, n):
    if s[i - 1] == 'W':
        e.append (e[-1] + 1)
    else:
        e.append (e[-1])

s_mir = s[::-1]
for j in range (1, n):
    if s_mir[j - 1] == 'E':
        w.append (w[-1] + 1)
    else:
        w.append (w[-1])
w = w[::-1]
total = set()
for k in range (n):
    total.add (e[k] + w[k])

print (min (total))