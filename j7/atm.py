b = '5687'
s = 0

while s < 3  :
    aa = int(input('enter password:'))
    a = str(aa)
    if len(a) == 4:
        if a == b:
            print('welcome')
            break
        
        elif a == b[::-1]:
            print('call the polic')
            break

        else:
            print('not welcome')
            s += 1
    else:
        print('try again')