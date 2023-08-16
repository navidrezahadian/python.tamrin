a = (52 ,'navid','navid','m','m', 2 , 1.54 ,'258na')
b = [11,22,33,44,55,66,77,88]

print('a =',a)
print('b =',b)
print()

list = list(a)
tuple = tuple(a)
set = set(a)
dict = dict(zip(a,b))

print('list =',list)
print('set =',set)
print('tuple =',tuple)
print('dict =',dict)