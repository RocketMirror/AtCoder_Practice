s = input()
l = [0, 0]

for i in range (len(s)):
    if s[i] == '0':
        l[0] += 1
    else:
        l[1] += 1

print (min(l) * 2)
