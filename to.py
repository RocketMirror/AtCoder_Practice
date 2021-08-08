import itertools

n = input()
l = [int (i) for i in list(str(n))]     #各桁をリスト化
wa = 0

for j in range (len(l)):   #各桁の和 
    wa += l[j]

if wa % 3 == 0:     #最初から３の倍数
    print (0)
    exit()

for k in range (1, len(n)):     #各桁から１〜len(n)-1ずつ組み合わせをとる
    kumi = list(itertools.combinations(l, k))
    for o in range (len(kumi)):     #組み合わせを一個ずつ見ていく
        if (wa - sum(kumi[o])) % 3 == 0:    #和から引いて３の倍数なら
            print(k)                         #引き抜いた桁数をプリント
            exit()
else:               
    print(-1)       #全て試して無理なら−１プリント
