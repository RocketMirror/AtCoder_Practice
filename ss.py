s = input()
if len(s) % 2 != 0:
    s = s[:-1]
    if s[:len(s)//2 + 1] == s[len(s)//2 + 1:]:
        print (len(s))
        exit()
else:
    if s[:len(s)//2] == s[len(s)//2:]:
        s = s[:-2]
while s[:len(s)//2] != s[len(s)//2:]:
    s = s[:-2]
print (len(s))
    