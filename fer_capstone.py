from fer import FER
import cv2
import time
emotion_detector = FER()
cap = cv2.VideoCapture(0)
emotion="empty"

def fun():
    while True:
        ret, input_image = cap.read()
        if not ret:
            continue
        input_image = cv2.resize(input_image, (640,480), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        input_image = cv2.GaussianBlur(input_image,(3,3),1)

        emotion = emotion_detector.detect_emotions(input_image)
        top_emotion = emotion_detector.top_emotion(input_image)
        # emotion, score = emotion_detector.top_emotion(input_image)
        # score = str(score)
        
        if(emotion is not None):
            # emotion = emotion + " : " + score
            print(emotion)
            # input_image = cv2.putText(input_image, emotion + " : " + score, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
            # cv2.imshow('Window', input_image)
            cv2.waitKey(100)
            break
    return emotion, top_emotion

fun()
# cap.release()
# cv2.destroyAllWindows()