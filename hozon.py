n = int (input())
s = set()
cnt = 0

while True:
    cnt += 1
    
    if n % cnt == 0:
        s.add (cnt)
        s.add (n // cnt)
        m = n // cnt
    if cnt >= m:
        break

print (*sorted(s), sep = '\n')