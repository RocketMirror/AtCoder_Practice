n = int (input())
a = list (map (int, input().split()))
b = [0]
for i in a:
    b.append (b[-1] + i)
del b[0]
print (b)
l = [b[0], [0, 0]]
for j in range (1, len(b)):
    for k in range (j):
        if ((b[j] - b[j - k]) % 200) in l:
            ind = l.index ((b[j] - b[j - k]) % 200)
            x = l[ind + 1][0] - l[ind + 1][1] 
            xlist = [i + 1 for i in range (l[ind + 1][1] - l[ind + 1][0], l[ind + 1][1] + 1)]
            y = j - k
            ylist = [e + 1 for e in range (j - k + 1, j + 1)]
            print (x + 1, *xlist,'\n',y + 1, *ylist)
            exit()

        else:
            l.append (b[j] - b[j - k] % 200)
            l.append ([j, k])
    