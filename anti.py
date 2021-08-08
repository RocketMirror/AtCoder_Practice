import math
a, b, c, d = map (int, input().split())
lcm = c * d // math.gcd (c, d)
x = b // c + b // d - b // lcm - ((a - 1) // c + (a - 1) // d - (a - 1) // lcm)
print (b - a + 1 - x)