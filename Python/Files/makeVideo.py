import cv2
import glob


timeList = [0, 30, 47, 60, 76, 85, 93, 101, 133, 148, 160, 168, 176, 186, 196, 204, 211, 223, 247]

frameList = []
for i in range(len(timeList)):
    if i==0:
        continue
    frameList.append(timeList[i]-timeList[i-1])

print(len(frameList))
frameSize = (1470, 980)
out = cv2.VideoWriter('../../Videos/test.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize)
idx = 0
for filename in glob.glob('../..//Images/*.jpg'):
    for i in range(frameList[idx]):
        img = cv2.imread(filename)
        out.write(img)
    idx += 1

out.release()