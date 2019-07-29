import os
import cv2

for f in os.listdir('Images/full_catAndDog'):
    if f.split('.')[-1] == 'txt': continue
    img = cv2.imread('Images/full_catAndDog/'+f)
    print(img)
    if len(img[1]) > 1300 or len(img[0]) > 800:
        os.rename('Images/full_catAndDog/'+f,'tmp/'+f)
