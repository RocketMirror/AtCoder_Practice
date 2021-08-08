s = input()
ss = list (reversed (s))
for i in range (len(s)):
    if s[i] == 'A':
        a = i
        break

for j in range (len(s)):
    if ss[j] == 'Z':
        z = j
        break

print(len(s)-a-z)
