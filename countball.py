n, a, b = map (int, input().split())
remain = n % (a + b)
num = n // (a + b)
print (num * a + remain if remain <= a else num * a + a)