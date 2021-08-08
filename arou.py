n = int (input())

for i in range (1, 100001):
    x = i ** 2
    if x > n:
        print ((i - 1) ** 2)
        exit()