# Python program to translate 
# speech to text conversion

import speech_recognition as sr
import pyttsx3 
import apiai
# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech 
def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init('dummy') 
	engine.say(command) 
	engine.runAndWait() 
	
	
# Loop infinitely for user to speak 
text_length=0
# It will going to continue run until it count the text length less than 80.
while(text_length<80):	
	
	# Exception handling to handle 
	# exceptions at the runtime 
	try: 
		
		# use the microphone as source for input. 
		with sr.Microphone() as source2: 
			
			# wait for a second to let the recognizer 
			# adjust the energy threshold based on 
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2) 
			
			#listens for the user's input 
			audio2 = r.listen(source2) 
			
			# Using google to recognize audio 
			MyText = r.recognize_google(audio2) 
			MyText = MyText.lower() 

			print("Message: \n"+MyText) 
			SpeakText(MyText) 
			text_length=len(MyText)
			print(text_length)
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
		
	except sr.UnknownValueError: 
		print("try again!, You were not clear last time ")

