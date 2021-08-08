n = str (input())

if len(n) == 1:
    print (n)
    exit()

cnt = 0
for i in range (1, len(n)):
    if n[i] == '9':
        cnt += 1
    else:
        break
    if cnt == len(n) - 1:
        print (int(n[0]) + 9 * (len(n) - 1))
        exit()
    

top = int (n[0]) - 1
bot = 9 * (len(n) - 1)

print (top + bot)

