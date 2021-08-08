n = int(input())
a = list (map (int, input().split()))
cost = 0
cost_ = 0
total = sum(a)
heikin, heikin_ = total // n, total // n + 1
for i in a:
    cost += (i - heikin) ** 2
    cost_ += (i - heikin_) ** 2
print (min (cost, cost_))