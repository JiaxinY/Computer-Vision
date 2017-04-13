import sys
import skimage
import os
from skimage import io
import scipy.misc as sp
import numpy as np
import matplotlib.pyplot as mpl
import math

#load image
img = str(sys.argv[1])
ucsd = io.imread(img)
out_name1 = img.split(".")[0] + "_rotate_90.png"
out_name2 = img.split(".")[0] + "_rotate_180.png"
out_name3 = img.split(".")[0] + "_rotate_270.png"

#image rotation function:
def rotate_image(image, angle):

    #initialize new image to empty numpy array
    size = image.shape
    new_image = np.empty([size[0],size[1],size[2]])

    #move each pixel to a new spot based on transformation
    for x in range(size[0]):
        for y in range(size[1]):
            newX = int(math.cos(angle)*x - math.sin(angle)*y)
            newY = int(math.sin(angle)*x + math.cos(angle)*y)
            new_image[newX][newY] = image[x][y]
    return new_image

#anticlockwise 3pi/2
img1 = rotate_image(ucsd, math.pi/2)

#anticlockwise pi
img2 = rotate_image(ucsd, math.pi)

#anticlockwise pi / 2
img3 = rotate_image(ucsd, 3 * math.pi / 2)

#save images to output files
mpl.imshow((np.uint8(img1)))
mpl.savefig(out_name1)

mpl.imshow((np.uint8(img2)))
mpl.savefig(out_name2)

mpl.imshow((np.uint8(img3)))
mpl.savefig(out_name3)