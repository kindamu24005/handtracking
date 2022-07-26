# import cv2
# import mediapipe as mp
# import time

# # キャプチャーするwebカメラの設定
# # ウィンドウズに内蔵されているのカメラアプリを使うので()の中は0
# cap = cv2.VideoCapture(0)

# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils

# # FPSを表示させる
# # 以前の時間
# pTime = 0
# # 現在の時間
# cTime = 0


# # カメラアプリを起動するコード
# while True:
#     success, img = cap.read()
#     # 画像をRGBに変換
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
#     # print(results.multi_hand_landmarks)

#     # もしresults.multi_hand_landmarksがTrueなら（何か値をとったら）
#     if results.multi_hand_landmarks:
#         # 認識した手の数だけforで回す
#         for handLms in results.multi_hand_landmarks:

#             for id, lm in enumerate(handLms.landmark):
#                 # print(id, lm)
#                 # h:高さ、w:幅、c:チャンネル
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x*w), int(lm.y*h)
#                 # print(id, cx, cy)
                
#                 # 特定のポイントを巨大化させる
#                 # if id == 12:
#                 #     cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
#                 # if id == 8:
#                 #     cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)



#             # ここはRGBイメージじゃなく、オリジナルイメージを使う
#             # mpHands.HAND_CONNECTIONSは各ポイントを繋ぐ
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

#     # # FPSの計算
#     # cTime = time.time()
#     # fps = 1/(cTime - pTime)
#     # pTime = cTime

#     # # FPSを表示させる
#     # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#     #             (255, 0, 255), 3)


#     cv2.imshow("Image", img)
#     cv2.waitKey(1)