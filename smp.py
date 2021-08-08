n, m, t = map (int, input().split())
juden = 0
bb = 0      #前回のカフェの退店時間
nokori = n
shinnokori = n

for i in range (m):
    a, b = map (int, input().split())
    shouhi = a - bb     #カフェに入るまでの消費

    if nokori - shouhi <= 0:    #残量０の場合終了
        print ('No')
        exit()

    juden = b - a       #カフェでの充電量
    shinnokori = nokori - shouhi + juden    #もろもろ終えての残量

    if shinnokori > n:      #バッテリー容量を超えていた場合
        shinnokori = n

    nokori = shinnokori     #残量の引き継ぎ
    bb = b      

if nokori <= t - b:     #最後のカフェを退店してからの消費
    print ('No')
else:
    print('Yes')