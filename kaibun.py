def kaibun (x):
    h = len(x) // 2
    if len(x) % 2 == 0:
        if x[:h] == x[h:][::-1]:
            return True
        else:
            return False
    else:
        if x[:h] == x[h + 1:][::-1]:
            return True
        else:
            return False
s = str (input())

sa = s[:(len(s) - 1) // 2]
sb = s[(len(s) + 3) // 2 - 1 : len(s)]
cnt = 0

if kaibun(s):
    cnt += 1
if kaibun(sa):
    cnt += 1
if kaibun(sb):
    cnt += 1

if cnt == 3:
    print ('Yes')
else:
    print ('No')

    