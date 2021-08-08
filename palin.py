n = str (input())
for i in range (len(n)):
    if n[-1] == '0':
        n = n[:-1]
    else:
        break
    
n_mir = n[::-1]
n_mir = n_mir [: len(n_mir) // 2] 
n = n[: len(n) // 2]

print ('Yes' if n == n_mir else 'No')