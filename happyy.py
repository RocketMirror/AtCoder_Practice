n = int (input())
a = list (map (int, input().split()))
dic = dict()
for i in range (1, min (2**n, 202)):
    total = 0
    for shift in range (n):
        if i >> shift & 1:
            total += a[shift]
    total = total % 200

    if total in dic:
        b = dic[total]
        c = i
        blist = []
        clist = []
        for j in range (n):
            if b >> j & 1:
                blist.append (j + 1)
            if c >> j & 1:
                clist.append (j + 1)
        print ('yes')
        print (len(blist), *blist)
        print (len(clist), *clist)
        exit()
    else:
        dic[total] = i 
print ('no')
