n, x = map(int, input().split())
s = list(input())

for i in s:
    if i == 'o':
        x += 1
    else:
        x -= 1
    
    if x < 0:
        x = 0

print (x)