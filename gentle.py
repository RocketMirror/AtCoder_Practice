n = int(input())
l = []
cnt = 0

for i in range (n):     #座標入力しリストに保存
    xy = list(map(int, input().split())) 
    l.append(xy)

for j in range (n - 1):
    for k in range (j + 1, n):
            x = l[k][0] - l[j][0]   #xの増加量
            y = l[k][1] - l[j][1]   #yの増加量

            if - 1 <= y / x and y / x <= 1:
                cnt += 1

print (cnt)