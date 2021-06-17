for i in range(1,15):
    filename = 'example'+str(i)+'.jpg'
    print(filename)
    img = load_image(filename)
    imshow(img)
 
    detector = get_fruit_detector()
    objects_result = detect_fruit(detector, img)
    get_fruit_result(detector)
