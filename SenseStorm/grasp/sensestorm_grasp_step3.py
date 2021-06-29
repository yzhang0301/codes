motor_grab = Motor("D")
ultra_sensor = UltrasonicSensor("1")
distance = ultra_sensor.get_distance()
print('distance: ',distance)
