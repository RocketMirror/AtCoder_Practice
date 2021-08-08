n = int (input())
b = 0
b_cnt = 0

for a in range (1, n):
    b = (n - 1) // a
    b_cnt += b

print (b_cnt)