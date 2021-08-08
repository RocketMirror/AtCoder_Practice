n = int (input())
a = max (list (map (int, input().split())))
b = min (list (map (int, input().split())))
print (b - a + 1 if b >= a else 0)