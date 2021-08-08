n = int (input())
a = list(map(int,input().split()))
gcd = 0
maxk = 0

for i in range (2, 1001):
    cnt = 0
    for j in range (n):
        if a[j] % i == 0:
            cnt += 1     
    if cnt >= gcd:
        gcd = cnt
        maxk = i
    
print (maxk)