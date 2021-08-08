n, m = map (int, input().split())
a = list (map (int, input().split()))
a = list(filter (lambda x: x >= sum(a) * 1 / (4 * m), a))
print ('Yes' if len(a) >= m else 'No')