my_list_1 = {11,22,33,22,22,123,123}

print()
print('my list 1 = ' , my_list_1)
my_list_1.add(999)
print('my list 1 add 999 = ' , my_list_1)
my_list_1.update([11,22,5555])
print('my list 1 update 11,22,5555 = ' , my_list_1)
my_list_1.remove(33)
print('my list 1 remove 33 = ' , my_list_1)
my_list_1.discard(11)
print('my list 1 discard 11 = ' , my_list_1)
print()

my_list_2 = (11,22,33,22,22,123,123)

print('my list 2 = ' , my_list_2)
print('my list 2 count (22) = ', my_list_2.count(22))
print('my list 2 index (33) = ', my_list_2.index(33))
print()

my_list_3 = {'ali':18 , 'navid':21 , 'hasan':15 , 'sine':16}

print('my list 3 = ', my_list_3)
print('my list 3 get ali = ' , my_list_3.get('ali'))
print('my list 3 pop navid = ' , my_list_3.pop('navid'))
x = my_list_3.copy()
print('my list 3 copy x = ' , x)
my_list_3.update({'sara':17})
print('my list 3 update sara:17 = ' , my_list_3)
my_list_3.clear()
print('my list 3 clear = ' , my_list_3)
print()