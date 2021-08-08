import math
r, x, y = map (int, input().split())
dis = (x ** 2 + y ** 2) ** 0.5
if dis < r:
    print (2)
else:
    print (math.ceil (dis / r))