motor_c = Motor("C")
def door_control(speed,p_time):
 if speed>0:
   speak("Opening")
 if speed<0:
   speak("Closing")
 motor_c.run_time(speed,p_time)
  
while True:
 frame = get_image()
 position = detect_face(frame)
 if position is not None:
   door_control(30,0.5)
   sleep(5)
   door_control(-30,0.5)
   sleep(2)
