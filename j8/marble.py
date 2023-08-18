import random

sum = 0
marble = 0

while marble != 6:
    
    marble = random.randint(1 , 6)
    print(marble)
    sum += marble

print('sum marble = ', sum)