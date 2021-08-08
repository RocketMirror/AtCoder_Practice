import math
import decimal
a, b, c, d = map (int, input().split())
aa, bb = a - c, b - d
kyori = ((a - c) ** 2 + (b - d) ** 2) ** 0.5 / (2 ** 0.5)

kakudo = math.atan2 (bb, aa) - math.radians (45.0)

ox, oy = kyori * math.cos (kakudo) + c, kyori * math.sin (kakudo) + d

e, f = ox - (a - ox), oy - (b - oy)
g, h = ox - (c - ox), oy - (d - oy)
print (round(e), round(f), round(g), round(h))