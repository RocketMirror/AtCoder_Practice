import itertools
n, m, x = map (int, input().split())
skill =[]
price = []
for i in range (n):     #skill,priceに記録
    ca = list (map (int, input().split()))
    a = ca[1 : m + 1]
    c = ca[0]
    skill.append (a)
    price.append (c)

check = [[0, 1]] * n        #それぞれの本を買ったか0or1で判定
pro = list (itertools.product (*check))
price_list = []

for q in pro:       #本を買うパターンをまわす
    skill_sum = [0] * m
    price_sum = 0
    cnt = 0
    for p in range (n):     #本の冊数をまわす
        if q[p] == 1:      #買った本の炙り出し
            price_sum += price[p]       #買った本の値段をプラスする
            for s in range (m):     #アルゴリズム毎の理解度をプラスする
                skill_sum[s] += skill[p][s]

    for t in skill_sum:     #全てのアルゴリズムで理解度が達しているか判定
        if t >= x:
            cnt += 1
        if cnt == m:
            price_list.append (price_sum)   #達していれば合計金額を記録
        
if len (price_list) == 0:   #理解度が達さなければ−１を出力
    print (-1)
else:
    print (min (price_list))    #合計金額の最小値を出力