from deepface import DeepFace
from PIL import Image 
from cv2 import cv2
from matplotlib import pyplot as plt
img_path = 'C:/Users/RAHUL/Desktop/DESKTOP/id proofs/Webp.net-compress-image.jpg'
img = cv2.imread(img_path)
plt.imshow(img[:,:,::-1])
image = Image.open(img_path)
image.show()
print(img)
abhishek = DeepFace.analyze(img_path)
print("Age : ",abhishek["age"])
print("Gender : ",abhishek["gender"])
print("Emotion : ",abhishek["dominant_emotion"])
print("Race : ",abhishek["dominant_race"])
