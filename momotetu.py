h, w = map (int, input().split())
l = [str (input()) for _ in range (h)]
dp = [[0 for _ in range (w)] for _ in range (h)]

#高橋を＋、青木をーで点数化
def color(y, x):
    if y == 0 and x == 0:
        return 0
    elif (y + x) % 2 == 0:
        if l[y][x] == '+':
            return -1
        else:
            return 1
    else:
        if l[y][x] == '+':
            return 1
        else:
            return -1

#マスを逆順で全探索
for y in range (h - 1, -1, -1):
    for x in range (w - 1, -1, -1):
        #初期値設定
        if y == h - 1 and x == w - 1:
            dp[y][x] = color(y, x)
            continue
        #例外処理
        if y == h - 1:
            dp[y][x] = dp[y][x + 1] + color(y, x)
            continue
        elif x == w - 1:
            dp[y][x] = dp[y + 1][x] + color(y, x)
            continue
        #原則処理
        if (y + x) % 2 == 0:
            dp[y][x] = max (dp[y + 1][x] + color(y, x), dp[y][x + 1] + color(y, x))
        else:
            dp[y][x] = min (dp[y + 1][x] + color(y, x), dp[y][x + 1] + color(y, x))

if dp[0][0] > 0:
    print ('Takahashi')
elif dp[0][0] < 0:
    print ('Aoki')
else:
    print ('Draw')