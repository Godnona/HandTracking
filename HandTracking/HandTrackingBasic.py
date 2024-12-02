import cv2
import mediapipe as mp
import time

# cv2
cam = cv2.VideoCapture(0)
cam.set(3, 1280)
cam.set(4, 720)

# media pipe
mpHands = mp.solutions.hands
hands = mpHands.Hands() # initialize obj
mpDraw = mp.solutions.drawing_utils

# time
pTime = 0
cTime = 0

while True:
    isRead, img = cam.read()
    if not isRead:
        print("Error load image frame !")
        break
    img = cv2.flip(img, 1)

    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img)
    if results.multi_hand_landmarks:
        for handLmk in results.multi_hand_landmarks:
            for id, lmk in enumerate(handLmk.landmark):
                # print(id, lmk)
                h, w, c = img.shape
                cx, cy = int(lmk.x * w), int(lmk.y * h)

                # print(id, cx, cy)

                cv2.circle(img, (cx, cy), 10, (255, 0, 225), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLmk, mpHands.HAND_CONNECTIONS)

    # fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 ,255), 2)

    # create window
    cv2.imshow("Python", img)
    cv2.waitKey(1)
