frame = None
videostream = cv2.VideoCapture(0)
def read_frame():
    global frame
    imW = videostream.get(cv2.CAP_PROP_FRAME_WIDTH)
    imH = videostream.get(cv2.CAP_PROP_FRAME_HEIGHT)
    while True:
        ret,frame = videostream.read()
        show_image(frame)

def display_video():
    Thread(target=read_frame,args=(),daemon=True).start()

display_video()

def face_parameter():
    global frame
    location = detect_face(frame)
    if location is not None:
        print(location)
        left = location[0]
        right = location[2]
        target_x = (left+right)/2
        width = right - left
        return target_x,width
    else:
        return None,None
