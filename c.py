n, m = map (int, input().split())
pl = []
sl = []
collect = 0
shinwrong = 0

for k in range (m):
    p, s = input().split()
    pl.append (int(p))
    sl.append (s)

for i in range (1, n + 1):
    wrong = 0
    for j in range (m):
        if pl[j] == i:
            if sl[j] == 'AC':
                collect += 1
                shinwrong += wrong
                break
            if sl[j] == 'WA':
                wrong += 1
    



print (collect, shinwrong)
