n = int (input())
ac, wa, tle, re = 0, 0, 0, 0
for i in range (n):
    s = str (input())
    if s == 'AC':
        ac += 1
    elif s == 'WA':
        wa += 1
    elif s == 'TLE':
        tle += 1
    else:
        re += 1
print ('AC x', ac,'\n' 'WA x', wa,'\n' 'TLE x', tle,'\n' 'RE x', re)