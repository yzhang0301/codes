#Threaded Sorting
from CourseHeader.API import *
from threading import Thread
from time import sleep
import cv2

frame = None
videostream = cv2.VideoCapture(0)
def read_frame():
    global frame
    while True:
        ret,frame = videostream.read()
        show_image(frame)
    
motor_belt = Motor("A")
motor_sort = Motor("B")

def convey_short():
    motor_belt.run_angle(0.5, -0.6)
    sleep(2)
    
def convey_long():
    motor_belt.run_angle(0.5, -1.2)
    sleep(3)

def left_sort():
    motor_sort.run_angle(0.5, -1.01)
    sleep(2)

def right_sort():
    motor_sort.run_angle(0.5, 1)
    sleep(2)
    
def display_video():
    Thread(target = read_frame, args = (), daemon = True).start()

display_video()
while True:
    try:
        colorlist = get_frame_color(frame)
        if colorlist is not None:
            color = colorlist[0]
            if color == "Black":
                print("Color is not found")
            else: 
                print(color, "is found!")
                if color == "Yellow":
                    convey_short()
                    right_sort()
                elif color == "Green":
                    convey_short()
                    left_sort()
                elif color == "Red":
                    convey_long()
                    right_sort()
                elif color == "Blue":
                    convey_long()
                    left_sort()
    except:
        break            
cv2.destroyAllWindows()
videostream.release()
