n, C = map (int, input().split())
event = []
for i in range (n):
    a, b, c = map (int, input().split())
    b = b + 1
    event.append ([a, c])
    event.append ([b, -c])
event.sort()
total = []
day = 0
price = 0
ans = 0
for x, y in event:
    if x != day:
        ans += min (C, price) * (x - day)
        day = x
    price += y
print (ans)