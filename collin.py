import itertools
import math
l = []

n = int(input())

for i in range (n):
    xy = list(map (int,input().split()))
    l.append(xy)

com = list(itertools.combinations(l, 3))

for j in range (n*(n-1)*(n-2)//6):
    if com[j][0][0] - com[j][1][0] == 0:
        if com[j][2][0] == com[j][0][0]:
            print('Yes')
            exit()
        else:
            continue
    katamuki = (com[j][0][1]-com[j][1][1]) / (com[j][0][0]-com[j][1][0])
    seppen = com[j][0][1] - katamuki * com[j][0][0]
    if com[j][2][1] == round(katamuki * com[j][2][0] + seppen, 10):
        print('Yes')
        exit()

else:
    print('No')

###---------------------------------------------------------

import itertools
la = []
lb = []

N = int(input())
xs = []
ys = []
for i in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xcom = list(itertools.combinations(xs, 2))
ycom = list(itertools.combinations(ys, 2))

ways = int(N*(N-1)/2)
consts = []
for j in range(ways):
    cnt = 0
    if xcom[j][1] - xcom[j][0] != 0:
        a = (ycom[j][1]-ycom[j][0])/(xcom[j][1]-xcom[j][0])
        b = ycom[j][0] - a*xcom[j][0] 
    else:
        for o in xs:
            if o == xcom[j][0]:
                cnt += 1
                if cnt >= 3:
                    print('Yes')
                    exit()    

    la.append(a)
    lb.append(b)

for k in range(ways):
    point = 0
    a = la[k]
    b = lb[k]
    for l in range(N):
            
        if ys[l] == round(a*xs[l] + b, 10):
            point += 1
            if point == 3:
                print('Yes')
                exit()
    
if point != 3 :
    print('No')
