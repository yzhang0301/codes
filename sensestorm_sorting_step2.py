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

while True:
    try:
        frame = get_image()
        show_image(frame)
        colorlist = get_frame_color(frame)
            
        if colorlist is not None:
            # convey_color(colorlist)
            color = colorlist[0]
            if color == 'Black':
                continue
            else:
                print(color,' is found!')
                convey_object[color][0]()
                convey_object[color][1]()
     
    except:
        print(sys.exc_info())
        break

'''
#while True:
frame = get_image()
show_image(frame)
color = get_frame_color(frame)
print("color is: ", color)
'''

'''    
    color = color_sensor.get_color()
    print(color)
    if color == 'Black':
        pass
    else:
        convey_object[color][0]()
        convey_object[color][1]()
    sleep(1)
'''

#convey_short()
