import itertools
s = list (str (input()))
hairu = []
hairan = []
wakaran = []
for i in range (10):
    if s[i] == 'o':
        hairu.append(i)
    elif s[i] == 'x':
        hairan.append(i)
    else:
        wakaran.append(i)

l = [0,1,2,3,4,5,6,7,8,9]

pro = itertools.product(l, repeat= 4)

c = 0
n = len (hairan)
cnt = 0

for p in pro:
    c = 0
    n = len (hairan)
    
    if len(hairu) == 0:
        if len(hairan) == 0:
            print (10000)
            exit()
            

        for r in hairan:
                if r not in p:
                    n -= 1
                if n == 0:
                    cnt += 1

    for h in hairu:
        if h in p:
            c += 1
        if c == len(hairu):
            if len (hairan) == 0:
                cnt += 1

            for r in hairan:
                if r not in p:
                    n -= 1
                if n == 0:
                    cnt += 1
print (cnt)