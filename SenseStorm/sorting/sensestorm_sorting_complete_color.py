from CourseHeader.API import *
from time import sleep

motor_belt = Motor("A")
motor_sort = Motor("B")
color_sensor = ColorSensor("1")

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

while True:
    color = color_sensor.get_color()
    if color == "Black" or color is None:
        continue
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
