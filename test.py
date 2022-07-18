import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    # もしresults.multi_hand_landmarksがTrueなら（何か値をとったら）
    if results.multi_hand_landmarks:
        # 認識した手の数だけforで回す
        for handLms in results.multi_hand_landmarks:
            # ここはRGBイメージじゃなく、オリジナルイメージを使う
            # mpHands.HAND_CONNECTIONSは各ポイントを繋ぐ
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Image", img)
    cv2.waitKey(1)