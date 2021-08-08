n = int(input())
com = (len(str(n)) - 1) // 3
ans = 0
for i in range (1, com + 1):
    m = n
    ans += m - 1000 ** i + 1
print (ans)

