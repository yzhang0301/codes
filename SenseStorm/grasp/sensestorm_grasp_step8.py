from sensestorm import Motor, UltrasonicSensor
from time import sleep
from CourseHeader.utils.HandDetector import detect_gesture
from CourseHeader.API import *

motor_grab = Motor("D")
motor_move = Motor("A")

global grab_flag
grab_flag = False

gesture_list = ["OK","V","THUMB_UP","STOP","TICK","HEART","GRAB","FIST","FIST_PALM_SALUTE","SINGLE_HAND_HEART","FOREFINGER_UP", "SIX","PALMS_TOGETHER"]

angle_init = motor_move.get_angle()
print('angle: ',angle_init)

def reset():
    angle = motor_move.get_angle() - angle_init
    print('angle: ',angle)
    motor_move.run_angle(0.5, angle/360)
    ultra_sensor = UltrasonicSensor("1")
    distance = ultra_sensor.get_distance()
    print('distance: ',distance)

def grab():
    global grab_flag
    if not grab_flag:
        motor_grab.run_time(50, 0.5)
        sleep(1)
        grab_flag = True

def release():
    global grab_flag
    if grab_flag:
        motor_grab.run_time(-50, 0.5)
        sleep(1)
        grab_flag = False

def draw_bounding_box(frame, location):
    cv2.rectangle(frame, (location[0],location[1]), (location[2],location[3]), (10, 255, 0), 2)
 
def draw_label(frame, location, label):
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
    label_ymin = max(location[1], labelSize[1] + 10) # Make sure not to draw label too close to top of window
    cv2.rectangle(frame, (location[0], label_ymin-labelSize[1]-10), (location[0]+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
    cv2.putText(frame, label, (location[0], label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text

videostream = cv2.VideoCapture(0)
while True:
    try:
        ret,frame = videostream.read()
        frame = cv2.flip(frame, 1)
        gesture,location  =  detect_gesture(frame)
        print("gesture index is: ",gesture)
        speak(gesture_list[int(gesture)])
        if gesture is not None:
            x_center = (location[0] + location[2])/2
            print(x_center)
            location = [int(x) for x in location]
            draw_bounding_box(frame, location)
            draw_label(frame, location, str(gesture))
            time.sleep(0.1)
        
        show_image(frame)
 
        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break
    except:
        print(sys.exc_info())
        break
# Clean up
print("clean")
cv2.destroyAllWindows()
videostream.release()
