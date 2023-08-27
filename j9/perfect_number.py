number = int(input('number = '))
a = 0 

for i in range(1 , number):
    if number % i == 0:
        a += i

if a == number :
    print('number = perfect number')
else:
    print('number = not perfect number')