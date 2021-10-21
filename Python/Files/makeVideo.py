import cv2
# import numpy as np
import glob

frameSize = (1470, 980)

out = cv2.VideoWriter('../../Videos/test.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize)

for filename in glob.glob('../..//Images/*.jpg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()