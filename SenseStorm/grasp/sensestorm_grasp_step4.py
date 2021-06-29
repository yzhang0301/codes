motor_grab = Motor("D")

global grab_flag
grab_flag = False
global left_flag
left_flag = True

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
def smart_hand():
    ultra_sensor = UltrasonicSensor("1")
    distance = ultra_sensor.get_distance()
    print(distance)
    if distance < 8 and distance > 3:
        grab()
        sleep(2)
        release()

while True:
  	smart_hand()
