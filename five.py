import math
n = int (input())
a = int (input())
b = int (input())
c = int (input())
d = int (input())
e = int (input())
small = min (a, b, c, d, e)
print (math.ceil(n / small - 1 + 5))