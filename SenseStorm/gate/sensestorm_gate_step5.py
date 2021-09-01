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
