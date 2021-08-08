s = sorted(input())
t = sorted(input(), reverse= True)
l = [s, t]
l.sort()
if s == t:
    print('No')
elif l[0] == s:
    print('Yes')
else:
    print('No')
