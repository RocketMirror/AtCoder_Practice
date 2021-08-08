import math
a, b, h, m = map (int, input().split())
tall = math.radians (6 * m)
short = math.radians (30 * h + 30 * 1 / 60 * m)
print ((a ** 2 + b ** 2 - 2 * a * b * math.cos (tall - short)) ** 0.5)