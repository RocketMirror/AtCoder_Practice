def eratos (n):
    num = set()
    prime = []
    for i in range (2, n + 1):
        if i not in num:
            prime.append (i)
        for j in range (i * i, n + 1, i):
            num.add (j)
    return prime, len (prime)

a, b = eratos (10)
print (*a, b)

            