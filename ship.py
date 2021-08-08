n, m, q = map (int, input().split())
wv = [list(map (int, input().split())) for _ in range (n)]
wv = sorted (wv, key= lambda e: -e[1]) 
x = tuple(map (int, input().split()))
for i in range (q):
    cnt = 0
    l, r = map (int, input().split())
    copy = list (x)
    for j in range (l - 1, r):
        copy[j] = 0
    copy = sorted (copy)
    
    for k in range (len(wv)):
        for o in range (len(copy)):
            if copy[o] < wv[k][0]:
                continue
            else:
                cnt += wv[k][1]
                copy[o] = 0
                
                break
    print (cnt)

# 294351 18291  13
# 847725 708774 6
# 629542 694643 7
# 266181 363342 10
# 561719 19130  12
# 589629 873953 1
# 400157 816803 3
# 503001 853040 2
# 348643 101338 11
# 446671 804773 4
# 360906 593889 8
# 872778 367931 9
# 916678 755919 5