s = input()
s = s[::-1]

def owari ():
    if s == '':
        print ('YES')
        exit()

while True:
    if s [0 : 6] == 'resare':
        ss = s.replace ('resare', '', 1)
        s = ss
        owari()

    elif s [0 : 7] == 'remaerd':
        ss = s.replace ('remaerd', '', 1)
        s = ss
        owari()

    elif s [0 : 5] == 'esare':
        ss = s.replace ('esare', '', 1)
        s = ss
        owari()

    elif s [0 : 5] == 'maerd':
        ss = s.replace ('maerd', '', 1)
        s = ss
        owari()

    else:
        print ('NO')
        exit()
