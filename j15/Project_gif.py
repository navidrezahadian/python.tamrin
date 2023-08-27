import imageio.v2 as imag2
import os

images = []

for file_name in os.listdir('emtehan\image'):
    img = imag2.imread('emtehan\image'+ '/'  + file_name)
    images.append(img)

imag2.mimsave('emtehan\gift\m.gif', images)