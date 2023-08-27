prime = []

for i in range(2 , 100):
   if i > 1:
       for j in range(2 , i):
           if (i % j) == 0:
               break
       else:
           prime.append(i)

print('prime 0 to 100 = ' , prime)