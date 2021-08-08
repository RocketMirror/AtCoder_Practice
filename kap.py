n, k = list(map (int,input().split()))


for j in range (k):
    l = []
    i = n
    while i >= 1:
        l.append (i % 10)
        i = i // 10

    small = map (str,filter (lambda x: x != 0, sorted(l)))
    big = map (str,sorted (l, reverse = True))

    small = ''.join (small)
    big = ''.join (big)

    if small == '':
        small = '0'
    if big == '':
        big = '0'

    small = int (small)
    big = int (big)

    a = big - small
    n = a

print (n)