n = int(input())
N = 2 ** n
a = list (map (int, input().split()))
A = a

if n == 1:
    b = a
    jun = min(b)
    for k in range (N):
        if A[k] == jun :
            print (k + 1)
            exit()

for j in range (n - 1):
    b = []
    
    for i in range (N // 2):
        if a[i + i] > a[i + i + 1]:
            b.append(a[i + i])
        else:
            b.append(a[i + i + 1])
    
    a = b

    N = N // 2

jun = min(b)

for k in range (N):
    if A[k] == jun :
        print (k + 1)
        
