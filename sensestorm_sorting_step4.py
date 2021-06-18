motor_belt = Motor("A")
motor_sort = Motor("B")
color_sensor = ColorSensor("1")

def convey_short():
    motor_belt.run_angle(0.5, 0.6)
    sleep(2)
    
def convey_long():
    motor_belt.run_angle(0.5, 1.15)
    sleep(3)

def left_sort():
    motor_sort.run_angle(0.5, -1.01)
    sleep(2)

def right_sort():
    motor_sort.run_angle(0.5, 1)
    sleep(2)

convey_object = {
    'Yellow': [convey_short, right_sort],
    'Green': [convey_short, left_sort],
    'Red': [convey_long, right_sort],
    'Blue': [convey_long, left_sort]
}

color = color_sensor.get_color()
print(color)
if color == 'Black':
    pass
else:
    convey_object[color][0]()
    convey_object[color][1]()
    sleep(1)
