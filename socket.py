a, b = map (int, input().split())
plug = 1
cnt = 0
while plug < b:
    plug += a - 1
    cnt += 1
print (cnt)