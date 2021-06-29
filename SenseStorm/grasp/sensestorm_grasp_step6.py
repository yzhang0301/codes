motor_grab = Motor("D")
motor_move = Motor("A")

angle_init = motor_move.get_angle()
print('angle: ',angle_init)

def reset():
    angle = motor_move.get_angle() - angle_init
    print('angle: ',angle)
    motor_move.run_angle(0.5, angle/360)
    ultra_sensor = UltrasonicSensor("1")
    distance = ultra_sensor.get_distance()
    print('distance: ',distance)

motor_move.run_time(40, 0.5)
sleep(1)
reset()
