import qrcode
import cv2
img=qrcode.make("https://free-url-shortener.rb.gy/")
img.save("ABHISHEK YADAV1.jpg") 
d=cv2.QRCodeDetector()
val,points, straight_qrcode=d.detectAndDecode(cv2.imread("MY LINKEDIN.jpg"))
print(val)