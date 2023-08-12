a = int(input('enter number: '))
a = str(a)
b = 0
c = 0

if a.count('0'):
    b += a.count('0')
if a.count('2'):
    b += a.count('2')
if a.count('4'):
    b += a.count('4')
if a.count('6'):
    b += a.count('6')
if a.count('8'):
    b += a.count('8')
if a.count('1'):
    c += a.count('1')
if a.count('3'):
    c += a.count('3')
if a.count('5'):
    c += a.count('5')
if a.count('7'):
    c += a.count('7')
if a.count('9'):
    c += a.count('9')

print('tedad zoj :', b)
print('tedad fard :', c)

if b > c :
    print('zoj')
elif c>b:
    print('fard')
else:
    print('=')