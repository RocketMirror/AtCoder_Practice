a, b, c = map (int, input().split())
for i in range (a, 10**7, a):
    if i % b == c:
        print ('YES')
        exit()
print ('NO')