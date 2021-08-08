l = int (input())
n = 1
m = 1

for i in range (1, 12):
    n *= i

for j in range (l - 11, l):
    m *= j

print (m // n)