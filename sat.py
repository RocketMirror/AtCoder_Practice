n = int (input())
l = set()

for i in range (n):
    s = str (input())
    l.add (s)

for j in l:
    if '!' + j in l:
        print (j)
        exit()

print ('satisfiable')