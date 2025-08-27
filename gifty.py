import imageio as iio
from PIL import Image
import numpy as np

pic_names=['E:\\third.jpg','E:\\second.jpg','E:\\last.jpg']
images=[]

base_image=Image.open(pic_names[0])
size=base_image.size
# in line 8 we picked an image from our list of images (pic_names) so than in line 9 we can use that image as a base-
#to resize the rest of the images to be the same size as the image we picked,bc if all images arent the same size-
#it will cause errors when u turn them into a gif
for pic in pic_names:
    im=Image.open(pic).resize(size)
    images.append(np.array(im))
#np.array() converts image into a numerical NumPy array which is required for the (.mimsave()) fuction to handle-
#image data efficiently for GIF creation

#Lastly, let’s use the .imwrite() method to turn the images into a GIF:
iio.mimsave('shame.gif',images,duration=500,loop=0)
#important note:when u pick the name of the file u must add the (.gif) extension 


#images: The list containing the image data.
#duration = 500: How long each picture should show in the GIF, in milliseconds.
#loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).