import cv2
import pyttsx3
import threading

# 初始化語音引擎
engine = pyttsx3.init()
engine.setProperty('rate', 130)

# 門牌語音播放函式


def speak_room():
    engine.say("七零一零八教室")
    engine.runAndWait()


# 載入 Haar 模型
cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(1) #外接攝影機
said = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    signs = cascade.detectMultiScale(gray, 1.3, minNeighbors=3, minSize=(150, 150),
                                     maxSize=(350, 350))

    if len(signs) > 0:
        for (x, y, w, h) in signs:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "70108", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if not said:
            # 啟動語音播放新執行緒
            threading.Thread(target=speak_room).start()
            said = True
    else:
        said = False

    cv2.imshow("Detecting", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
