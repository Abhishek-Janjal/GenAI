import cv2 # type: ignore
import numpy as np # type: ignore
import handtracking as htm
import time
import pyautogui # type: ignore
import math

##########################
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7
#########################

plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()


while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        zx1,zy1=lmList[4][1],lmList[4][2]
        zx2,zy2=lmList[8][1],lmList[8][2]
        length=math.hypot(zx2-zx1,zy2-zy1)
        print(length)

        fingers = detector.fingersUp()


        if fingers[1] == 1:

            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            pyautogui.moveTo(x3,y3)
            pyautogui.mouseUp()


        if fingers[1] == 1 and fingers[2] == 1:

            length, img, lineInfo = detector.findDistance(8, 12, img)

            if length < 40:
                pyautogui.mouseDown()
        
        if fingers[0] == 1 and fingers[1] == 1:
            if length<30:
                pyautogui.scroll(-3)
            elif length>100:
                pyautogui.scroll(3)


        #area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        #     if area<130:
        #         pyautogui.scroll(-5)
        #     elif area>270:
        #            pyautogui.scroll(5)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()
