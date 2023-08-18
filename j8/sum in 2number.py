a = int(input('number a: '))
b = int(input('number b: '))
c = 0 

if a > b:
    for i in range(b , a+1):
        c += i
    print(c)

elif b > a:
    for i in range(a , b+1):
        c += i
    print(c)
        
else:
    print('0')