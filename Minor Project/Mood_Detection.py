# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:02:15 2021

@author: Tanmoyee
"""

import cv2
import numpy as np
from tensorflow.keras.models import load_model


prototxt_path='models/deploy.prototxt.txt'
caffemodel_path='models/weights.caffemodel'

print("Loading models...")
face_model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
emotion_model=load_model("./models/fer2013_mini_XCEPTION.102-0.66.hdf5",compile=False)
print("Done")


target_size=emotion_model.input_shape[1:3]
emotion_labels={0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'sad', 5: 'surprise', 6: 'neutral'}
color={0: (0,0,255), 1: (0,0,100), 2: (230,200,0), 3: (0,255,0), 4: (100,0,0), 5: (0,255,255), 6: (255,0,255)}


def detect_emotion(image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image=cv2.resize(image,(target_size))
    input1=np.float32(image)
    input1=input1/255.0;
    input1=input1-0.5
    input1=input1*2.0
    input1=np.expand_dims(input1,0)
    input1=np.expand_dims(input1,-1)
    output=emotion_model.predict(input1)
    return np.argmax(output);


def process(image):
    #image = cv2.imread(image)
    (h, w) = image.shape[:2]
    output=image.copy()
    blob = cv2.dnn.blobFromImage(cv2.resize(image.copy(), (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_model.setInput(blob)
    detections = face_model.forward()
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence>0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            frame=image[startY:endY, startX:endX]
            emotion=detect_emotion(frame)
            text = emotion_labels[emotion]
            y = startY - 10 if startY - 10 > 10 else startY + 10
            res=cv2.rectangle(output, (startX, startY), (endX, endY),color[emotion], 2)
            cv2.putText(output, text, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color[emotion], 2)
            '''while True:
                cv2.imshow("Emotion detection", output)
                if cv2.waitKey(1) & 0xFF == ord('a'):
                    break'''
    return output


def real_time_feed(video):
    cap=cv2.VideoCapture(video)
    res,frame=cap.read()
    print(frame.shape)
    print("Press 'a' to stop...")
    while(True):
        res,frame=cap.read()
        if frame is None:
            break
        output=process(frame)
        cv2.imshow("Emotion detection", output)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    cap.release()
    cv2.destroyAllWindows()
