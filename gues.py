n, m = map (int, input().split())
s_list = []
c_list = []
for i in range (m):
    s, c = map (int, input().split())
    s_list.append (s)
    c_list.append (str(c))

num = ['x'] * n

for j in range (m):
    if s_list[j] > n:
        print (-1)
        exit()
    if num[s_list[j] - 1] == 'x':
        num[s_list[j] - 1] = c_list[j]
    else:
        if num[s_list[j] - 1] == c_list[j]:
            continue
        else:
            print (-1)
            exit()

if len (num) == 1 and num[0] == 'x':
    print (0)
    exit()
if len (num) == 1 and num[0] == '0':
    print (0)
    exit()

if num[0] == '0':
    print (-1)
    exit()
elif num[0] == 'x':
    num[0] = '1'
for e in range (1, n):
    if num[e] == 'x':
        num[e] = '0'
print (''.join (num))