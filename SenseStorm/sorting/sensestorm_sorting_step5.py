from CourseHeader.API import *

motor_belt = Motor("A")
motor_sort = Motor("B")
color_sensor = ColorSensor("1")

def convey_short():
    motor_belt.run_angle(0.5, 0.6)
    sleep(2)
    
def convey_long():
    motor_belt.run_angle(0.5, 1.2)
    sleep(3)

def left_sort():
    motor_sort.run_angle(0.5, -1.01)
    sleep(2)

def right_sort():
    motor_sort.run_angle(0.5, 1)
    sleep(2)

def get_frame():
    videostream = cv2.VideoCapture(0)
    ret, frame = videostream.read()
    frame = cv2.flip(frame, 1)
    cv2.destroyAllWindows()
    videostream.release()
    return frame    

convey_object = {
    'Yellow': [convey_short, right_sort],
    'Green': [convey_short, left_sort],
    'Red': [convey_long, right_sort],
    'Blue': [convey_long, left_sort]
}

while True:
    frame = get_frame()
    show_image(frame)
    color = get_frame_color(frame)
    print("color is: ", color)
