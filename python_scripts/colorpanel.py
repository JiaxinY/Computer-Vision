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
cleese = io.imread(img)
out_name = "colorpanel_" + img.split(".")[0] + ".png"

#resize cleese image to 256 x 256 pixels
resize_cleese = sp.imresize(cleese,(256,256))

#initialize empty numpy arrays of the correct size
green = np.empty([256,256,3])
blue = np.empty([256,256,3])
red = np.empty([256,256,3])

#create loop control variables
i = 0
j = 0

#parse resized image pixel by pixel
for row in resize_cleese:
    j = 0
    for pixel in row:
        green[i][j] = [0, pixel[1], 0]
        blue[i][j] = [0, 0, pixel[2]]
        red[i][j] = [pixel[0], 0, 0]
        j += 1
    i += 1

#create new image containing the original, and then the single color channels
cleese_final = np.empty([512, 512, 3])
for i in range(512):
    for j in range(512):
        if i < 256 and j < 256:
            cleese_final[i][j] = resize_cleese[i][j]
        elif i < 256 and j > 256:
            cleese_final[i][j] = green[i][j-256]
        elif i > 256 and j < 256:
            cleese_final[i][j] = red[i-256][j]
        else:
            cleese_final[i][j] = blue[i-256][j-256]

mpl.imshow((np.uint8(cleese_final)))
mpl.savefig(out_name)
