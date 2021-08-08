a, b = map (int,input().split())
c, d = map (int,input().split())

if a == c and b == d:#最初から目的地
    print (0)
    exit()
elif a + b == c + d or a - b == c - d or abs (a - c) + abs (b - d) <= 3:#あと一手で目的地
    print (1)
    exit()
elif c + (b + c - a) == c + d or c - (b + c - a) == c - d or abs (c - c) + abs (b + c - a - d) <= 3:#cに近づけるように右上左下に動かす
    print (2)
    exit()
elif c + (b - (c - a)) == c + d or c - (b - (c - a)) == c - d or abs (c - c) + abs (b - (c - a) - d) <= 3:#cに近づけるように右下左上に動かす
    print (2)
    exit()
elif a + 3 + b == c + d or a + 3 - b == c - d or abs (a + 3 - c) + abs (b - d) <= 3:#右に３マス動かす
    print (2)
    exit()
elif a - 3 + b == c + d or a - 3 - b == c - d or abs (a - 3 - c) + abs (b - d) <= 3:#左に３マス動かす
    print (2)
    exit()
elif a + b + 3 == c + d or a - (b + 3) == c - d or abs (a - c) + abs (b + 3 - d) <= 3:#上に３マス動かす
    print (2)
    exit()
elif a + b - 3 == c + d or a - (b - 3) == c - d or abs (a - c) + abs (b - 3 - d) <= 3:#下に３マス動かす
    print (2)
    exit()
elif (a + b) % 2 == (c + d) % 2:#斜め移動２回で行ける場合
    print (2)
    exit()
else:   
    print (3)#以上で到達しない場合
    exit()
