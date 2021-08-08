import itertools
a = [1,3,4,5,6,7,8,3]

b = list (map (lambda x: x ** 2, a))
print (b)

c = [str(int(i ** 0.5)) for i in a]
print (''.join (c))

d = list (filter(lambda y: y-5 > 0, a))
[print (z) for z in d]

p = list(itertools.permutations ([o for o in range (3)]))
[print (pp) for pp in p]