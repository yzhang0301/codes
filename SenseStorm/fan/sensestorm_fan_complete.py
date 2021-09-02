from CourseHeader.API import *
from CourseHeader.utils.FaceDetector import detect_face
from threading import Thread
from time import sleep
import sys
import traceback


frame = None
location =None
label = "face"
videostream=cv2.VideoCapture(0)
def read_frame():
    global frame
    while True:
        ret,frame = videostream.read()
        show_image(frame)
 

def draw_label_boundingbox(frame,location,label):
    location = [int(x) for x in location]
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
    label_ymin = max(location[1], labelSize[1] + 10)
    cv2.rectangle(frame, (location[0], label_ymin-labelSize[1]-10), (location[0]+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED)
    cv2.rectangle(frame, (location[0],location[1]), (location[2],location[3]), (10, 255, 0), 2)
    cv2.putText(frame, label, (location[0], label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    show_image(frame)

label = "face"
def face_parameter():
    global frame
    global location
    location = detect_face(frame)
    if location is not None:
        draw_label_boundingbox(frame,location,label)
        print("location ",location)
        left = location[0]
        right = location[2]
        target_x=(left+right)/2
        width = right - left
        return target_x,width
    else:
        return None,None

def direction_judge(target_x):
    motor_c = Motor("C")
    print("target_x ",target_x)
    if target_x and target_x < 200:
        motor_c.run_time(-35,0.01)
    elif target_x and target_x > 450:
        motor_c.run_time(35,0.01)
    sleep(0.5)

def distance_judge(width):
    motor_a = Motor("A")
    if width > 280:
        motor_a.run_time(40,1)
    elif width > 180:
        motor_a.run_time(60,1)
    elif width > 100:
        motor_a.run_time(80,1)
        
def fan_tracking():
    target_x,width = face_parameter()
    if width:
        distance_judge(width)
    if target_x:
        direction_judge(target_x)
def display_video():
    Thread(target=read_frame, args=(), daemon=True).start()

display_video()
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
