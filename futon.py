h, w = map (int, input().split())
ss = ['#'] * w
cnt = 0

for i in range (h):
    s = list(input())

    for j in range (w-1):      #行
        if s[j] == '.' and s[j+1] == '.':
            cnt += 1   

    for k in range (w):       #列
        if ss[k] == '.' and s[k] == '.':
            cnt += 1
    
    ss = s
print (cnt)