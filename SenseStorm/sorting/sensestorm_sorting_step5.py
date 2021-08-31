from threading import Thread
import cv2

frame=None
videostream = cv2.VideoCapture(0)
def read_frame():
    global frame
    imW = videostream.get(cv2.CAP_PROP_FRAME_WIDTH)
    imH = videostream.get(cv2.CAP_PROP_FRAME_HEIGHT)
 while True:
        ret,frame = videostream.read()
        show_image(frame)

def display_video():
    Thread(target=read_frame,args=(),daemon=True).start()

display_video()
while True:
    try:
        colorlist = get_frame_color(frame)
        print(colorlist)
    except:
        break

clean_up()
