n = int (input())
a = list(map (int, input().split()))
b = list(map (int, input().split()))
leng = len(a)
ans = 0

for i in range (leng):
    nai = a[i] * b[i]
    ans += nai

if ans == 0:
    print('Yes')
else:
    print('No')