n = str (input())
if len (n) == 1:
    print (0)
    exit()
if len(n) % 2 == 0:
    x = int (n[:len(n)//2])
    y = int (n[len(n)//2:])
    print (x if x <= y else x - 1)
else:
    print ('9' * (len(n) // 2))