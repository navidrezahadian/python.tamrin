a = str(input('enter str:'))

#   afzayesh tol reshte va gharar dadanesh dar vasat
b = a.center(18)
print('center :',b)

#   tamom shodan reshte ba karakter khas
c = a.endswith('d')
print('endswith :',c)

#   chek kardan in ke tamam reshte fasele hast
d = a.isspace()
print('isspace :',d)

#    tashkhis horof bodan reshte
s = a.isalpha()
print('isalpha :',s)