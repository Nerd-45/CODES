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
