from CourseHeader.API import *
from CourseHeader.utils.FaceDetector import detect_face
from threading import Thread
from time import sleep
import sys
import traceback


frame = None
target_x = None
videostream = cv2.VideoCapture(0)
def read_frame():
    global frame
    global videostream
    while True:
        ret,frame = videostream.read()
        show_image(frame)

def face_parameter():
    global frame
    location = detect_face(frame)
    if location is not None:
        print(location)
        left,top,right,bottom = location[0:4]
        target_x=(left+right)/2
        width = right - left
        return target_x,width
    else:
        return None,None
target_x,width = face_parameter()
print("target_x and width is: ",target_x,width)

motor_c = Motor("C")
def direction_judge():
    global target_x
    while True:
        print(target_x)
        if target_x and target_x < 200:
            motor_c.run_time(-35,0.01)
        elif target_x and target_x > 450:
            motor_c.run_time(35,0.01)
        sleep(0.5)

direction_judge_thread = Thread(target=direction_judge, args=(), daemon=True)
direction_judge_thread.start()

motor_a = Motor("A")
def distance_judge(width):
    if width > 280:
        motor_a.run_time(40,1)
    elif width > 180:
        motor_a.run_time(60,1)
    elif width > 100:
        motor_a.run_time(80,1)
        
def fan_tracking():
    global target_x
    target_x,width = face_parameter()
    if width:
        distance_judge(width)

read_frame_thread = Thread(target=read_frame, args=(), daemon=True)
read_frame_thread.start()

while True:
    try:
        fan_tracking()
    except:
        print(sys.exc_info())
        break

# Clean up
print("clean")
cv2.destroyAllWindows()
videostream.release()
