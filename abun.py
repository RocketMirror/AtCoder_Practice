n = int (input())
a = list (map (int,input().split()))

for i in range (1, n + 1):     #kのパターン
    big = 0
    for j in range (n - i + 1):     #基準点
        total = sum (a[j : j + i])      
        if big < total:
            big = total 
    print (big)
