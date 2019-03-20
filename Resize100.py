# 15-184 Image resizing exercise practice
# Write a script which d'resize all images in a directory to 100x100

import glob2    # needed a venv pip3 install glob2
import os       # could've imported on 1 line
import cv2

os.chdir('.')       # this directory (to make sure)
for file in glob2.glob('*.jpg'):
    img = cv2.imread(file, 0)
    resized_img = cv2.resize(img, (100, 100))        # size must be tuple
    resized_name = os.path.splitext(os.path.basename(file))[0] + '__resized' + os.path.splitext(os.path.basename(file))[1]
    cv2.imwrite(resized_name, resized_img)
