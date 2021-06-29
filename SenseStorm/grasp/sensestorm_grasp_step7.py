from CourseHeader.utils.HandDetector import detect_gesture
from CourseHeader.API import *

motor_grab = Motor("D")
motor_move = Motor("A")

global grab_flag
grab_flag = False

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

videostream = cv2.VideoCapture(0)
while True:
    try:
        ret,frame = videostream.read()
        frame = cv2.flip(frame, 1)
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
