n = int (input())

m = 10 ** n - (9 ** n + 9 ** n - 8 ** n)

print (m % (1000000000 + 7))