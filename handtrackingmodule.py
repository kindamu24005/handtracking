import cv2
import mediapipe as mp
import time



class handDetector():

    # Hands()のパラメータを__init__()のパラメータに書く
    def __init__(self, mode=False, modelcomplexity=1, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.modelComplex = modelcomplexity
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        # 画像をRGBに変換
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        # もしresults.multi_hand_landmarksがTrueなら（何か値をとったら）
        if self.results.multi_hand_landmarks:
            # 認識した手の数だけforで回す
            for handLms in self.results.multi_hand_landmarks:
                # ここはRGBイメージじゃなく、オリジナルイメージを使う
                # mpHands.HAND_CONNECTIONSは各ポイントを繋ぐ
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                # h:高さ、w:幅、c:チャンネル
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                
                lmList.append([id, cx, cy])

                # if draw:
                #     cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

        
        return lmList


def main():
    
    
    # キャプチャーするwebカメラの設定
    # ウィンドウズに内蔵されているのカメラアプリを使うので()の中は0
    cap = cv2.VideoCapture(0)

    # FPSを表示させる
    # 以前の時間
    pTime = 0
    # 現在の時間
    cTime = 0

    detector = handDetector()

    # カメラアプリを起動するコード
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        # # FPSの計算
        # cTime = time.time()
        # fps = 1/(cTime - pTime)
        # pTime = cTime

        # # FPSを表示させる
        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
        #             (0, 0, 0), 3)


        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()