import statistics
n = int(input())
a = list (map (int, input().split()))
l = []
for i in a:
    l.append (i + 1)
    l.append (i)
    l.append (i - 1)

print (l.count(statistics.mode (l)))