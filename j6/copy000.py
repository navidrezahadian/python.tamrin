color = ['blue','red','yellow','green','black']
colorstr = "blue red yellow green black"

x = color.copy()
print('copy',x)

color.insert(2,'white')
print('insert',color)

a = colorstr.index("green")
print ('index',a)

color.extend(['gray'])
print('extend',color)