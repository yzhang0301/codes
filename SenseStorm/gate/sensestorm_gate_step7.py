motor_c = Motor("C")
def door_control(speed,p_time):
  if speed>0:
    speak("Opening")
  if speed<0:
    speak("Closing")
  motor_c.run_time(speed,p_time)

while True:
  frame = get_image()
  feature1 = extract_feature(frame)
  if feature1 is None:
    print("Unable to extract features")
    speak("Unable to extract features")
    sleep(2)
  else:
    print("Features extracted, face registered")
    speak("Features extracted, face registered")
    sleep(2)
    break

while True:
  frame = get_image()
  feature2 = extract_feature(frame)
  if feature2 is not None:
    if compare_feature(feature1, feature2):
      print("Access granted")
      speak("Access granted")
      door_control(30,0.5)
      sleep(5)
      door_control(-30,0.5)
      sleep(2)
    else: 
      print("Access denied")
      speak("Access denied")
      sleep(2)
