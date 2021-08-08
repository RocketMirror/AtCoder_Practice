l, r = map (int, input().split())
ans = 2020
if r - l >= 2018:
    print (0)
    exit()
for i in range (l % 2019, r % 2019):
    for j in range (i + 1, r % 2019 + 1):
        if (i * j) % 2019 < ans:
            ans = (i * j) % 2019
        if ans == 0:
            print (0)
            exit()
print (ans)