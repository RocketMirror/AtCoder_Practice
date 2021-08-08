n = int (input())
a = list (map (int ,input().split()))
cnt = sum(a)
b = [a[0]]
for j in range (1, len(a)):
    b.append (b[-1] + a[j])

for i in range (n):
    if abs (b[i] - (b[-1]-b[i])) < cnt:
        cnt = abs (b[i] - (b[-1]-b[i]))
print (cnt)