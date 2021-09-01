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
      print("Same person")
      speak("Same person")
      sleep(2)
    else: 
      print("Different person")
      speak("Different person")
      sleep(2)
  else:
    print("Unable to extract new features")
    speak("Unable to extract new features")
    sleep(2)
