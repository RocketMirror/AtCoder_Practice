n, D, H = map (int, input().split())
d_list = []
h_list = []
for i in range (n):
    d, h = map (int, input().split())
    d_list.append (d)
    h_list.append (h)

ans = []
for j in range (n):
    y = (D * (H - h_list[j])) / (D - d_list[j]) - H + h_list[j]
    x = h_list[j] - y
    ans.append (x)

if max (ans) <= 0:
    print (0.0)
else:
    print (max (ans))


