print('c° to k° = enter 1')
print('c° to f° = enter 2')
print('k° to c° = enter 3')
print('k° to f° = enter 4')
print('f° to c° = enter 5')
print('f° to k° = enter 6')
print('exit = enter 7')

a = int(input('enter number :'))

while a != 7 :

    c = float(input('enter temp :'))

    if a == 1 :
        b = c + 273
    if a == 2 :
        b = c * 1.8 + 32
    if a == 3 :
        b = c - 273
    if a == 4 :
        b = (c - 273) * 1.8 + 32
    if a == 5 :
        b = (c - 32) * 5/9
    if a == 6 :
        b = (c - 32) * 1.8 + 273

    print(b)
    a = int(input('enter number :'))

    if a >= 7 :
        break