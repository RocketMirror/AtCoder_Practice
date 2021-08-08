import itertools
import math
n, m = map (int, input().split())
lab = []
for i in range (m):
    ab = list(map (int, input().split()))
    lab.append (ab)
lcd = []
k = int (input())
for j in range (k):
    cd = list (map (int, input().split()))
    lcd.append (cd)

pro = set (itertools.product (* lcd))

cnt_x = 0
for o in pro:
    o = set (o)
    cnt = 0
    for p in lab:
        if p[0] in o and p[1] in o:
            cnt += 1
    if cnt > cnt_x:
        cnt_x = cnt

print (cnt_x)