import cv2
import mediapipe as mp

class HandTracking:
    def __init__(self,
               static_image_mode=False,
               max_num_hands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        self.static_image_mode = False
        self.max_num_hands = 2
        self.model_complexity = 1
        self.min_detection_confidence = 0.5
        self.min_tracking_confidence = 0.5

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draws = mp.solutions.drawing_utils
        self.results = None

    def draw_hands(self, img, draw = True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            # print(self.results.multi_hand_landmarks)
            for handLmk in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draws.draw_landmarks(img, handLmk, self.mp_hands.HAND_CONNECTIONS)
        return img

    def get_landmark(self, img, draw = True, radius = 15, color = (255, 0, 255), thinkness = 2):
        list_lmk = []
        if self.results.multi_hand_landmarks:
            for handLmk in self.results.multi_hand_landmarks:
                for id, lmk in enumerate(handLmk.landmark):
                    h, w, c = img.shape
                    x, y = int(lmk.x * w), int(lmk.y * h)
                    list_lmk.append([id, x, y])

                    if draw:
                        cv2.circle(img, (x, y), radius, color, thinkness, cv2.FILLED)
        return list_lmk



def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 1080)
    cam.set(4, 720)

    hands_detect = HandTracking()

    while True:
        is_read, img = cam.read()
        img = cv2.flip(img, 1)

        hands_detect.draw_hands(img)


        cv2.imshow("Py", img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()