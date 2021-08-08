aa = list (map (str,input().split()))
ab = list (map (str,input().split()))
ac = list (map (str,input().split()))
n = int (input())
for i in range (n):
    b = str(input())
    for j in range (3):
        if aa[j] == b:
            aa[j] = '0'
        if ab[j] == b:
            ab[j] = '0'
        if ac[j] == b:
            ac[j] = '0'

if aa == ['0', '0', '0']:
    print ('Yes')
    exit()
if ab == ['0', '0', '0']:
    print ('Yes')
    exit()
if ac == ['0', '0', '0']:
    print ('Yes')
    exit()
if aa[0] == '0' and ab[1] == '0' and ac[2] == '0':
    print ('Yes')
    exit()
if aa[2] == '0' and ab[1] == '0' and ac[0] == '0':
    print ('Yes')
    exit()
if aa[0] == '0' and ab[0] == '0' and ac[0] == '0':
    print ('Yes')
    exit()
if aa[1] == '0' and ab[1] == '0' and ac[1] == '0':
    print ('Yes')
    exit()
if aa[2] == '0' and ab[2] == '0' and ac[2] == '0':
    print ('Yes')
    exit()

print ('No')