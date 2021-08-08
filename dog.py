l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ll = []
name = ''
n = int (input())
x = 0
for i in range (100):   #桁数とその桁数のスタートからの距離を出す
    x += 26 ** i
    if x > n:
        keta = i 
        start = x - 26 ** i
        plus = n - start
        break

for j in range (0, keta)[::-1]:     #各桁を出す
    ll.append (plus // 26 ** j)
    plus = plus % 26 ** j

for k in ll:    #各桁の数値をアルファベットに変換
    name += l[k]
print (name)