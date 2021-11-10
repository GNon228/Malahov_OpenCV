import cv2
import numpy as np
frameWidth =640
frameHeight =480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

#0,0,213,59,255,255- желтый
#24,42,107,167,94,182- фиолетовый
#91,13,116,131,43,152- серый
#0,201,226,179,255- красный
myColors= [[0,0,213,59,255,255],#желтый
           [24,42,107,167,94,182],#фиолетовый
           [0,201,226,179,255,255]]#красный

color_values = [[0,255,255],#желтый
           [255,0,255],#фиолетовый
           [0,255,255]]#красный
myPoints = []

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points=[]
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        # imgResult = cv2.bitwise_and(img, img, mask=mask)
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getCountours(mask)
        cv2.circle(imgResult,(x,y), 5, (0,255,255),cv2.FILLED)
        if x != 0 and y !=0:
            new_points.append([x,y,count])
        count += 1
    return new_points


       # cv2.imshow(str(color[0]),mask)
def getCountours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h= 0,0,0,0
    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area>1000:
           # cv2.drawContours(imgResult,contours,-1,(255,0,0),3,cv2.LINE_AA,hierarchy)
            peri = cv2.arcLength(cnt, True)#периметр
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            corner_count = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y
def drawOnCanvas(myPoints,my_col_val):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 5, my_col_val[point[2]], cv2.FILLED)


while True:
    succes, img = cap.read()
    img = cv2.flip(img,1)
    imgResult = img.copy()
    new_points = findColor(img,myColors)
    if len(new_points) != 0:
        for newP in new_points:
            myPoints.append(newP)
        if len(myPoints) != 0:
            drawOnCanvas(myPoints,color_values)
    # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #
    # lower = np.array([h_min, s_min, v_min])
    # upper = np.array([h_max, s_max, v_max])
    # imgResult  = cv2.bitwise_and(img,img,mask=mask)
    # mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("imgResult", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Esc =27
        break
#19,39,196,37,107,226- желтый
#24,42,107,167,94,182- фиолетовый
#91,13,116,131,43,152- серый
#0,201,226,179,255- красный

myColors= [[19,39,196,37,107,226],[24,42,107,167,94,182],[0,201,226,179,255],[91,13,116,131,43,152]]