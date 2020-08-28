from PIL import Image
import os


''' these are the inputs to be specified by user'''
# name of folder containing input images.
# Keep all the images in jpg or png format in the folder name mentioned
# do not put folders inside mentioned folder, paste all the images in the folder
inFolder = 'dataset/'

# name of folder containing input images
outFolder = 'converted/'

# dimensions of patches in pixels (number of pixels in image = input features)
height = 192
width = 256

''' now comes the real code '''
# get list of all images in dataset
inImages = os.listdir(inFolder)

# if output folder not present then create
if(outFolder[:-1] not in os.listdir()):
    os.mkdir(outFolder[:-1])

# make patches per image
for image in inImages:
    # Opens a image in RGB mode 
    im = Image.open(inFolder+image)

    # # Size of the image in pixels (size of orginal image) 
    xmax, ymax = im.size 
    # print(im.size,' dimensions of image file')

    xiter = width
    yiter = height
    idx = 0
    while(xiter<=xmax and yiter<=ymax):
        # Setting the points for cropped image 
        left = xiter-width
        top = yiter-height
        right = xiter
        bottom = yiter

        # Cropped image of above dimension 
        # (It will not change orginal image) 
        im1 = im.crop((left, top, right, bottom)) 

        # Shows the image in image viewer 
        # im1.show()

        # to save the image
        im1.save(outFolder+image.split('.')[0]+'_'+str(idx)+".jpg")
        im1.close()
        #incrementing variables
        idx += 1
        xiter += width
        yiter += height
    print(image,idx)