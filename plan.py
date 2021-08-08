n = int(input())
a = list(map(int,input().split()))
a = [0] + a + [0]
total = 0
for j in range (len(a) - 1):
    total += abs(a[j] - a[j + 1])

for i in range (1, n + 1):
    if a[i - 1] <= a[i] and a[i] <= a[i + 1]:
        print(total)
    else:
        print(total - ((abs(a[i - 1] - a[i]) + abs(a[i] - a[i + 1])) - abs(a[i - 1] - a[i + 1])))
