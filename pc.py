n = int(input())
t = list (map(int,input().split()))
m = int(input())
tt = t.copy()

for i in range (m):
    p, x = map(int,input().split())
    tt[p-1] = x 
    print (sum(tt))
    tt = t.copy()

