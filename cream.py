n = int (input())
s = set()
cnt = 0

for i in range (1, int(n ** 0.5) + 1):
    if n % i == 0:
        s.add (i)
        s.add (n // i)

print (*sorted(s), sep = '\n')
print (len(s))