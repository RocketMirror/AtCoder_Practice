n = int (input())
s = list (input())
q = int (input())
f = False
for i in range (q):
    t, a, b = list (map (int, input().split()))
    if t == 1:
        if f:
            if a > n:
                a = a - n
            else:
                a = a + n
            if b > n:
                b = b - n
            else:
                b = b + n
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    else:
        f = f == False

if f:
    s = s[n:] + s[:n]

print (*s, sep= '')

    

