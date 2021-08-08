h, w, x, y = map (int, input().split())
x = x - 1
y = y - 1
l = []
cnt = 0

for i in range (h):
    s = input()
    l.append(s[y])
    if i == x:
        for m in range (y):
            if s[y - m - 1] == '.':
                cnt += 1
            else:
                break
        for n in range (w - y - 1):
            if s[y + n + 1] == '.':
                cnt += 1
            else:
                break

for j in range (x):
    if l [x - j - 1] == '.' :
        cnt += 1
    else:
        break

for k in range (h - x - 1):
    if l [x + k + 1] == '.' :
        cnt += 1
    else:
        break

print (cnt + 1)

