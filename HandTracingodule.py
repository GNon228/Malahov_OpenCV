import mediapipe as mp
import time
from cv2 import cv2


class handDetector():
    def __init__(self,
                 mode=False,
                 maxHands=2,
                 complexity=1,
                 mdetectConf=0.5,
                 trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.mdetectConf = mdetectConf
        self.trackConf = trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,
                                        self.maxHands,
                                        self.complexity,
                                        self.mdetectConf,
                                        self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img,draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        # print(result.multi_hand_landmarks)
        hand_Landmarks = self.result.multi_hand_landmarks  # список меток ладоней

        if hand_Landmarks:
            for handLm in hand_Landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLm, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo =0,draw = True):
        lmList = []
        hand_Landmarks = self.result.multi_hand_landmarks  # список меток ладоней

        if hand_Landmarks:
            myHand = hand_Landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                 #
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                # print(id,cx,cy)
                if draw:
                    cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(100,0,100),2)
                 #print(id,(cx,cy),5,(0,0,255),cv2.FILLED)
                 #cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
        return lmList




def main():
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 0)

    pTime, cTime = 0, 0
    detector = handDetector()
    while True:
        succes, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        print(lmList)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Nigga", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Esc =27
            break


if __name__ == "__main__":
    main()
