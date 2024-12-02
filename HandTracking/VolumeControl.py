from sympy.physics.units import length

from MyModule import HandTrackingModule as Htm
from MyModule import MathModule as Math
import cv2
import time

# initialize camera
cam = cv2.VideoCapture(0)
cam.set(3, 1080)
cam.set(4, 720)

# initialize HandTrackingModule
hand_tracking = Htm.HandTracking()

# initialize time
previous_time = 0

while True:
    # Read image frame
    isRead, img = cam.read()
    if not isRead:
        print("Error to read image frame !")
    img = cv2.flip(img, 1)

    # Control volume
    hand_tracking.draw_hands(img)
    list_lmk = hand_tracking.get_landmark(img, False)

    if len(list_lmk) != 0:
        print(list_lmk[4][1], list_lmk[4][2])
        print(list_lmk[8][1], list_lmk[8][2])

        x1, y1 = list_lmk[4][1], list_lmk[4][2]
        x2, y2 = list_lmk[8][1], list_lmk[8][2]
        x0, y0 = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (250, 250, 100), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (250, 250, 100), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 25, 255), 3)

        cv2.circle(img, (x0, y0), 10, (250, 0, 100), cv2.FILLED)

        length = Math.hypotenuse(x2 - x1, y2 - y1)


    # Calculate fps
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    # Show fps
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 ,255), 2)

    # Create window
    cv2.imshow("TekMonk", img)
    if cv2.waitKey(1) == 27:  # Escape key
        break