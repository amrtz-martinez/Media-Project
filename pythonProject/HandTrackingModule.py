"""
HandTracingModule
By: Murtaza Hassan
Youtube: http: // www.youtube.com / c / MurtazasWorkshopRoboticsandAI
Website: https: // www.computervision.zone
"""

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, complex = 1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.complex = complex
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        #converts the colors of the image to rgb
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def fingerCounter(img, lmList, tips):
        totalFingers = 0
        # this starts when the list is not empty
        if len(lmList) != 0:
            fingers = []

            # checking if the thumb is open or closed
            if lmList[tips[0]][1] > lmList[tips[0] - 1][1]:
                # if thumb is open append 1
                fingers.append(1)
            else:
                # if thumb is closed append 0
                fingers.append(0)

            # checking if the 4 fingers are closed
            for id in range(1, 5):
                # checks if the finger is open or closed we do this by using mediapipe
                # to find the points detected on the fingers, we then compare the tip
                # of the finger to the middle of the finger.
                if lmList[tips[id]][2] < lmList[tips[id] - 2][2]:
                    # if the finger is open we append the value 1
                    fingers.append(1)
                else:
                    # if the finger is closed we append 0
                    fingers.append(0)

                # Counts the number of fingers on display
                totalFingers = fingers.count(1)

                # this section prints a square and number to show how many fingers are on display
                cv2.rectangle(img, (20, 255), (170, 380), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 25)

        return totalFingers

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList
