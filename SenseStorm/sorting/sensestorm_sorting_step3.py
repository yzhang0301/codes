motor_belt = Motor("A")
color_sensor = ColorSensor("1")

def convey_short():
    motor_belt.run_angle(0.5, 0.6)
    sleep(2)
    
def convey_long():
    motor_belt.run_angle(0.5, 1.2)
    sleep(3)

color = color_sensor.get_color()
print(color)
