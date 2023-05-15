from gpiozero import MotionSensor
import cv2
cam=cv2.VideoCapture(0)
img=cam.read()
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import email.encoders
import smtplib
import os
import email
import sys
import time

camera = opencv2()
pir = MotionSensor(4)
camera.rotation = 180 # delete or adjust to 90, 180, or 270 accordingly
h264_video = ".h264" 
mp4_video = ".mp4" 

while True:

    # record h264 video then save as mp4
    pir.wait_for_motion()
    video_name = datetime.now().strftime("%m-%d-%Y_%H.%M.%S")
    camera.start_recording(video_name + h264_video)
    pir.wait_for_no_motion()
    camera.stop_recording()
    os.system("MP4Box -add " + video_name + h264_video + " " + video_name + mp4_video) # tutorial for install to make this conversion possible at: http://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4
    os.system("rm " + video_name + h264_video) # delete h264 file
    footage = video_name + mp4_video

    # prepare the email
    f_time = datetime.now().strftime("%A %B %d %Y @ %H:%M:%S")
    msg = MIMEMultipart()
    msg["Subject"] = f_time
    msg["From"] = "your_address@gmail.com"
    msg["To"] = "to_address@gmail.com"
    text = MIMEText("WARNING! Motion Detected!")
    msg.attach(text)

    # attach mp4 video to email
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(footage, "rb").read())
    email.encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= %s" % os.path.basename(footage))
    msg.attach(part)

    # access Gmail account and send email
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("your_gmail_login","your_gmail_password")
    server.sendmail("your_address@gmail.com", "to_address@gmail.com", msg.as_string())
    server.quit()

    # delete mp4 from Pi after it has been emailed
    os.system("rm " + footage)
# set up PiCamera
camera = cv2.cv2()
camera.resolution = (320, 240)
 
# set up door sensor
door_sensor = digitalio.DigitalInOut(D5)
door_sensor.direction = digitalio.Direction.INPUT
 
# set up motion sensor
pir_sensor = digitalio.DigitalInOut(D6)
pir_sensor.direction = digitalio.Direction.INPUT
prev_pir_value = pir_sensor.value
is_pir_activated = False
 
# set up sgp30
i2c_bus = I2C(SCL, SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)
 
# set up the neopixel strip
pixels = neopixel.NeoPixel(D18, NUM_PIXELS_STRIP)
pixels.fill((0, 0, 0))
pixels.show()
