from collections import deque
k = int (input())
que = ['1','2','3','4','5','6','7','8','9']
x = 9
for q in que:
    if x > 100000:
        break
    x += 1
    a = q[-1]
    for i in [-1, 0, 1]:
        b = int(a) + i
        if b >= 0 and b < 10:
            que.append (q + str(b))
print (que[k - 1])

