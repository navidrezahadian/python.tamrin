import math

print('1 = bealave           2 = menha       3 = zarb        4 = tagsim')
print('5 = tagsim_sahih      6 = mod                         7 = darsad')
print('8 = sin               9 = cos        10 = tan        11 = cot')
print('12 = jazr            13 = tavan                      14 = ghadre_motlagh')
print('15 = log             16 = round_kardan               17 = kharej shodan')
print()

karbar = int(input('amal mored nazar = '))
print()

if karbar > 16 or karbar <= 0 :
    print('amali ba in adad mojod nist')

if karbar == 1 :
    a = float(input('a = '))
    b = float(input('b = '))
    print('bealave a,b = ' , a + b)

if karbar == 2 :
    a = float(input('a = '))
    b = float(input('b = '))
    print('menha a,b = ' , a - b)

if karbar == 3 :
    a = float(input('a = '))
    b = float(input('b = '))
    print('zarb a,b = ' , a * b)

if karbar == 4 :
    a = float(input('a = '))
    b = float(input('b = '))
    print('taghsim a,b = ' , a / b)

if karbar == 5 :
    a = float(input('a = '))
    b = float(input('b = '))
    print('taghsim_sahih a,b = ' , a // b)

if karbar == 6 :
    a = float(input('a = '))
    b = float(input('b = '))
    print('mod a,b = ' , a % b)

if karbar == 7 :
    a = float(input('adad kol = '))
    b = float(input('meghdar darsad = '))
    print('darsad = ' , a * (b / 100))

if karbar == 8 :
    a = float(input('sin(x), x = '))
    print('sin(x) = ' , math.sin(math.radians(a)))

if karbar == 9 :
    a = float(input('cos(x), x = '))
    print('cos(x) = ' , math.cos(math.radians(a)))

if karbar == 10:
    a = float(input('tan(x), x = '))
    print('tan(x) = ' , math.tan(math.radians(a)))

if karbar == 11 :
    a = float(input('cot(x), x = '))
    print('cot(x) = ' ,  1 / math.tan(math.radians(a)))

if karbar == 12 :
    a = float(input('a = '))
    print('jazr a = ' , a **(1/2))

if karbar == 13 :
    a = float(input('a = '))
    b = float(input('adad tavan = '))
    print('a tavan b = ' , a **(b))

if karbar == 14 :
    a = float(input('a = '))
    print('ghadre_motlagh a = ' , abs(a))

if karbar == 15 :
    a = float(input('a = '))
    b = float(input('paye log = '))
    print('log a = ' , math.log(a, b))

if karbar == 16 :
    a = float(input('a = '))
    print('round_kardan a = ' , round(a))

print()