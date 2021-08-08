n, a, b = map (int, input().split())
s = str (input())
cnt = 0
cnt_b = 0

for i in range (n):
    if s[i] == 'a':
        if cnt < a + b:
            print ('Yes')
            cnt += 1
            continue
        else:
            print ('No')
            continue
    if s[i] == 'b':
        if cnt < a + b and cnt_b + 1 <= b:
            print ('Yes')
            cnt += 1
            cnt_b += 1
            continue
        else:
            print ('No')
            continue
    if s[i] == 'c':
        print ('No')

    
