import cv2
import numpy as np
import face_recognition
import os
import pyttsx3
import mysql.connector 
import datetime

con = mysql.connector.connect(
    host="localhost",
    user = "root",
    password= "",
    database = "attendance"
)

mycursor = con.cursor()

time = datetime.datetime.now()

def register(name,course_code,key):

    sql = "INSERT INTO register(name,course_unit,time,key_code) VALUES (%s,%s,%s,%s)"
    val = (name,course_code,time,key)
    mycursor.execute(sql, val)
    con.commit()

def lecture_record(course_code,start,end,topic,key):
    sql = "INSERT INTO lecture_record(course_code,time,start,end,topic,key_code) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (course_code,time,start,end,topic,key)
    mycursor.execute(sql,val)
    print("lecture recorded succesfully")
    con.commit()


# engine = pyttsx3.init()




# def speak(name):
#     engine.say(name+" Registered successfully")
#     engine.runAndWait()

# # from PIL import ImageGrab

# path = 'd:/new projects/attendance system/class/checkk/static/assest/Training_images'

# images = []
# classNames = []
# myList = os.listdir(path)
# print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)


# def findEncodings(images):
#     encodeList = []


#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList


# encodeListKnown = findEncodings(images)
# print('Encoding Complete')

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
# # img = captureScreen()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# # print(faceDis)
#         matchIndex = np.argmin(faceDis)

#         if matches[matchIndex]:
#             name = classNames[matchIndex].upper()
# # print(name)
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#             subject = "math"
#             register(name,subject)
#             speak(name)
            
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break

#     cv2.imshow('Webcam', img)
#     cv2.waitKey(1)