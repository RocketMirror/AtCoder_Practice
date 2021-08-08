import heapq
n, m = map(int,input().split())
a = list(map(int,input().split()))
a = list(map(lambda x: x * (-1), a))
heapq.heapify(a)
for _ in range (m):
  small = heapq.heappop(a)
  heapq.heappush(a, -1 * (-small // 2))
print(-sum(a))
