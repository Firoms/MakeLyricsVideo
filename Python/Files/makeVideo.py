import cv2
import glob
import time

startTime = time.time()
print("start")
timeList = [0]
stop=''
while stop=='':
    stop = input()
    curTime = int((time.time()-startTime)//(0.25)+1)
    timeList.append(curTime-timeList[-1])
print(timeList)
timeList.append(12)
timeList.append(12)
timeList.append(12)



frameSize = (1470, 980)

out = cv2.VideoWriter('../../Videos/test.avi',cv2.VideoWriter_fourcc(*'DIVX'), 4, frameSize)

idx = 0
for filename in glob.glob('../..//Images/*.jpg'):
    idx += 1
    for i in range(timeList[idx]):
        img = cv2.imread(filename)
        out.write(img)

out.release()