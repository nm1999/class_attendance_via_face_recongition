from calendar import month
import datetime
import re
from django.shortcuts import render
import datetime
import cv2
import numpy as np
import face_recognition
import os
import pyttsx3
from checkk import main


date = datetime.datetime.now()
engine = pyttsx3.init()
# Create your views here.
def login(request):
    return render(request,'index.html')

def home(request):
    if request.method == "POST":
        course_code = request.POST.get("course_unit")
        start = request.POST.get("start")
        end = request.POST.get("end")
        topic = request.POST.get("topic")
        identifier = str(date.year)+str(date.month)+str(date.day)+course_code
        main.lecture_record(course_code,start,end,topic,identifier)
        # print(identifier)
        # from checkk import main
    
        def speak(name):
            engine.say(name+" Registered successfully")
            engine.runAndWait()

        # from PIL import ImageGrab

        path = 'd:/new projects/attendance system/class/checkk/static/assest/Training_images'

        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        print(classNames)


        def findEncodings(images):
            encodeList = []


            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList


        encodeListKnown = findEncodings(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
        # img = captureScreen()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
        # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    subject = course_code
                    main.register(name,subject,identifier)
                    speak(name)
                    
                    
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)
    return render(request,'home.html')

def newstd(request):
    if request.method == 'POST':
        pic = request.FILES['picture']
        print(pic)
        print("seen")
    return render(request,'newstudent.html')

def printout(request):
    return render(request,'printout.html')