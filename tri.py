n = int (input())
cnt = 0
l = [0] * 100000
for i in range (1, 100):
    for j in range (1, 100):
        for k in range (1, 100):
            m = i ** 2 + j ** 2 + k ** 2 + i*j + j*k + i*k
            l[m - 1] += 1

# for ans in range (n):
#     print (l[ans])
print(*[l[i] for i in range(n)], sep='\n')