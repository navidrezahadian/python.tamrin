use1 = 'nav'
use2 = 'ram'
use3 = 'caz'
use4 = 'moh'

pas1 = 'nn'
pas2 = 'rr'
pas3 = 'cc'
pas4 = 'mm'

a = str(input('enter use :'))
b = str(input('enter pas :'))

if a == use1 and b == pas1 :
    print('vorod mojaz')
elif a == use1 and b != pas1 :
    b = str(input('gheyr mojaz >> enter pas :'))
    if a == use1 and b == pas1 :
        print('vorod mojaz')
    else :
        print('vorod gheyr mojaz')
#////////////////////////////
if a == use2 and b == pas2 :
    print('vorod mojaz')
elif a == use2 and b != pas2 :
    b = str(input('gheyr mojaz >> enter pas :'))
    if a == use2 and b == pas2 :
        print('vorod mojaz')
    else :
        print('vorod gheyr mojaz')
#////////////////////////////
if a == use3 and b == pas3 :
    print('vorod mojaz')
elif a == use3 and b != pas3 :
    b = str(input('gheyr mojaz >> enter pas :'))
    if a == use3 and b == pas3 :
        print('vorod mojaz')
    else :
        print('vorod gheyr mojaz')
#////////////////////////////
if a == use4 and b == pas4 :
    print('vorod mojaz')
elif a == use4 and b != pas4 :
    b = str(input('gheyr mojaz >> enter pas :'))
    if a == use4 and b == pas4 :
        print('vorod mojaz')
    else :
        print('vorod gheyr mojaz')