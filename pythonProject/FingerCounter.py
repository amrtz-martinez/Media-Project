import cv2
import HandTrackingModule as htm

# setting the camera size
wCam, hCam = 640, 480
# accessing the camera
cap = cv2.VideoCapture(0)

# creating the size
cap.set(3, wCam)
cap.set(4, hCam)

# from mediapipe getting the tips of all the fingers
tipIds = [4, 8, 12, 16, 20]



# calling the detection
detector = htm.handDetector(detectionCon=0.75)

while True:
    # reads in the image from the camera
    success, img = cap.read()
    # cv2.flip(img, 1)
    # calls on the handTrackingModule to find the hand
    img = detector.findHands(img)
    # drawing the landmarks
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    # this starts when the list is not empty
    if len(lmList) != 0:
        fingers = []

        # checking if the thumb is open or closed
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
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
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
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

    cv2.imshow("Image", img)
    cv2.waitKey(1)

'''
# I think this is the code we would use to control the media player
    if totalFingers != 0:
        if totalFingers == 1:
            MediaPlayer.play()
        elif totalFingers == 2:
            MediaPlayer.nextSong()
        elif totalFingers == 3:
            MediaPlayer.previousSong()
        elif totalFingers == 4:
            MediaPlayer.pause(True)
        elif totalFingers == 5:
            MediaPlayer.pause(True)
'''
