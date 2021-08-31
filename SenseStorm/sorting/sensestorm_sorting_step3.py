color_sensor = ColorSensor("1")
while True:
  color = color_sensor.get_color()
  print(color)
