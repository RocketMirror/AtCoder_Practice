n = int(input())
p = list(map(int,input().split()))
s = set()
small = 0
up = 0

for i in p:
    s.add(i)
    if i > small or small > i:
        print (small)
        continue

    while small == i:
        up == small      #置き換え
        up += 1
        if up not in s:
            print(up)
            small = up      #戻す
            break
