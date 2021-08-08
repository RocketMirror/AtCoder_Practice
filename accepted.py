s = str(input())
def ex():
    print ('WA')
    exit()

if s[0] != 'A':
    ex()
s = 'x' + s[1:]
if s[2 : -1].count('C') != 1:
    ex()
s = s.replace ('C', '')
if not s.islower():
    ex()
print ('AC')