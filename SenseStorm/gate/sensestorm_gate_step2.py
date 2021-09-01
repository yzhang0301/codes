motor_c = Motor("C")
def door_control(speed,p_time):
  if speed>0:
    speak("Opening")
  if speed<0:
    speak("Closing")
  motor_c.run_time(speed,p_time)

door_control(30,0.5)
sleep(1)
door_control(-30,0.5)
