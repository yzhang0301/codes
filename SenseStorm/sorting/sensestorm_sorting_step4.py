while True:
    color = color_sensor.get_color()
    if color == "Black" or color is None:
        continue
    else: 
        print(color, "is found!")
        if color == "Yellow":
            convey_short()
            right_sort()
        elif color == "Green":
            convey_short()
            left_sort()
        elif color == "Red":
            convey_long()
            right_sort()
        elif color == "Blue":
            convey_long()
            left_sort()
