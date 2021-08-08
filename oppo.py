import math
n = int (input())
x_zero, y_zero = map (int, input().split())
x_half, y_half = map (int, input().split())
r = ((x_zero - x_half) ** 2 + (y_zero - y_half) ** 2) ** 0.5 / 2
o_x, o_y = (x_zero + x_half) / 2, (y_zero + y_half) / 2
x_zero, y_zero = x_zero - o_x, y_zero - o_y
atan_zero = math.atan2 (y_zero, x_zero)
atan_one = atan_zero + math.radians(360 / n)
print (math.cos(atan_one) * r + o_x, math.sin(atan_one) * r + o_y)