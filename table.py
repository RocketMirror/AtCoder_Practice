n = int(input())
ans = 10**50
for i in range (1,int(n**0.5) + 1):
    if n % i != 0:
        continue
    else:
        ans = min (ans, i + n // i)
print(ans - 2)