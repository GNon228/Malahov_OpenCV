import mediapipe as mp
import time
from cv2 import cv2
frameWidth =640
frameHeight =480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime, cTime = 0, 0

while True:
    succes, img = cap.read()
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)
    hand_Landmarks = result.multi_hand_landmarks #список меток ладоней

    if hand_Landmarks:
        for handLm  in hand_Landmarks:
            for id,lm in enumerate(handLm.landmark):
                print(id ,lm)
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)

                if id == 8:
                #print(id,(cx,cy),5,(0,0,255),cv2.FILLED)
                 cv2.circle(img,(cx,cy),5,(0,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img, handLm, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)),(10,50) ,cv2.FONT_HERSHEY_PLAIN , 3,(255,0,255),3)



    cv2.imshow("Nigga", img)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Esc =27
        break
