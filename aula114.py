# Count é um iterador sem fim

from itertools import count

c1 = count(8, 8)
r1 = range(8, 100, 8)

# print(next(c1))
# print(next(c1))
# print(next(c1))
# print(next(c1))

# print('c1', hasattr(c1, '__iter__'))
# print('c1', hasattr(c1, '__next__'))

# print('r1', hasattr(r1, '__iter__'))
# print('r1', hasattr(r1, '__next__'))

print('Count')

for i in c1:
    

    if i >= 100:
        print('')
        break
    
    print(i)

print('Range')

for i in r1:
    

    if i >= 100:
        print('')
        break
    
    print(i)





