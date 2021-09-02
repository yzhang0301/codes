def smart_fan(distance):
    if distance >= 20 and distance < 40:
        motor_a.run_time(40,10)
    elif distance >= 40 and distance < 60:
        motor_a.run_time(60,10)
    elif distance >= 60 and distance < 80:
        motor_a.run_time(80,10)
    else:
        motor_a.run_time(0,0)

ultra_sensor = UltrasonicSensor("1")
distance = ultra_sensor.get_distance()
print("distance is: ",distance)
smart_fan(distance)
