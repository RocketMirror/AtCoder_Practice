import math
n, k = map (int, input().split())
a = list (map (int, input().split()))

for i in range (n):     #１の位置
    if a[i] == 1:
        x = i
        break

left = x
right = n - 1 - x

if k - 1 <= right and k - 1 <= left:
    if left % 2 != 0 and right % 2 != 0 and k % 2 != 0:
        print (left // (k - 1) + right // (k - 1) + 1)
        exit()
        
    total = math.ceil(left / (k - 1)) + math.ceil(right / (k - 1))
    print (total)
else:
    total = math.ceil((n - k) / (k - 1)) + 1
    print (total)
