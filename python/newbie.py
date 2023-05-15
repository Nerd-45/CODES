# Importing required modules
# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# importing os module
import os


# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the password  is underprocess ='", Query, "'")
        except Exception as e:
            print(e)
            print("try that again sir ")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(2)
    return Query


# creating Speak() function to giving Speaking power
# to our voice assistant
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

Speak("speak out the password sir ?")
while True:
    command = take_commands()
    
    if "correct" in command:
        # Shutting down
        Speak("unlocking the door and  welcome ")
        #os.system("shutdown /s /t 30")
        break
    if "wrong" in command:
        Speak("wrong password sir ")
        break

    Speak("try that again sir ")

# OpenCV program to detect face in real time 
# import libraries of python OpenCV 
# where its functionality resides 
import cv2 

# load the required trained XML classifiers 
# data/haarcascades/haarcascade_frontalface_default.xml 
# Trained XML classifiers describes some features of some 
# object we want to detect a cascade function is trained 
# from a lot of positive(faces) and negative(non-faces) 
# images. 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# /data/haarcascades/haarcascade_eye.xml 
# Trained XML file for detecting eyes 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# capture frames from a camera 
cap = cv2.VideoCapture(0) 

# loop runs if capturing has been initialized. 
while 1: 

	# reads frames from a camera 
	ret, img = cap.read() 

	# convert to gray scale of each frames 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	# Detects faces of different sizes in the input image 
	faces = face_cascade.detectMultiScale(gray,1.3, 5) 

	for (x,y,w,h) in faces: 
		# To draw a rectangle in a face 
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
		roi_gray = gray[y:y+h, x:x+w] 
		roi_color = img[y:y+h, x:x+w] 

		# Detects eyes of different sizes in the input image 
		eyes = eye_cascade.detectMultiScale(roi_gray) 

		#To draw a rectangle in eyes 
		for (ex,ey,ew,eh) in eyes: 
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 

	# Display an image in a window 
	cv2.imshow('img',img) 

	# Wait for Esc key to stop 
	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
