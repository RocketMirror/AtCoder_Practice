import math
n = int(input())
x = list(map (int,input().split()))

print(sum (map (lambda i: abs(i), x)))
print(math.sqrt(sum (map (lambda j: j ** 2, x))))
print(max (map (lambda l: abs(l), x)))
