a, b, x = map (int, input().split())

for d in reversed (range (0, 10)):
    N_try = int ('1' + '0' * d)
    n = d + 1
    price = a * N_try + b * n
    if price <= x:
        N = (x - b * n) // a
        if N >= 1000000000 and len(str(N)) <= 10 and len(str(N)) > n: 
            print ('9' * n)
            exit()
        elif N >= 1000000000:
            print (1000000000)
            exit()
        else:
            print (N)
            exit()
print (0)