import cv2
import HandTrackingModule as htm

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
