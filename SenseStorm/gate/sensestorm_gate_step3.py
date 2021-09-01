frame = get_image()
show_image(frame)

position = detect_face(frame)
if position is None:
  print("No face detected")
  speak("No face detected")
else:
  print("Face detected")
  speak("Face detected")
