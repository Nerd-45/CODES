# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
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
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
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


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "hi" in command:
            Speak("hlo, how are you doing")
            break
    if "exit" in command:
            Speak("so sure ! as your wish, bye")
            # break
        # if "insta" in command:
        #     Speak("Best page on instagram is between twenty two yards")
        # if "learn" in command:
        #     Speak("search it down to learm")
        # if "code" in command:
        #     Speak("contact MR.Abhishek yadav ")
            
        #     break
        # if "creates" in command:
        #     Speak("Mr. Abhishek yadav ")
        #     break
        #  if "who are you " in command:
        #     Speak(" i am assistance created by Mr Abhishek yadav  ")
        #     break
        #  if " python" in command:
        #     Speak(" i am coded in python  ")
        #     break
        #  if "songs " in command:
        #     Speak(" you can use youtue to listen out the best of the songs  ")
        #     break
        #we can add such so many texts and the recommended dialouge to e spoken by the pc
        
