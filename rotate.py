# s = str(input())

# print(s[1], end = '')
# print(s[2], end = '')
# print(s[0])

s = list(input())
leng = len(s)
t = s[0]
s.remove (s[0])
s.insert (leng - 1, t)
print(''.join(s))
