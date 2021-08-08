a, b = map (str, input().split())
b = float (b)
b = round(b * 100)
a = int (a)

ab = str (a * b)
ans = ''
if len (ab) <= 2:
    print (0)
    exit()

for i in range (0,len (ab) - 2):
    ans += ab[i]

print (ans)