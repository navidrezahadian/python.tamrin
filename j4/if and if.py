a = float(input('enter namber :'))
c = a % 2
b = int(a % 10)

if c == 0 and b > 6 :
    print('A')
elif c == 0 and  b < 4 :
    print('B')
elif a < 0 :
    print('D')
else :
    print('C')