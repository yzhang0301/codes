from threading import Thread
import cv2

frame = None
videostream = None
def read_frame():
    global frame,videostream
    videostream = cv2.VideoCapture(-1)
    while True:
        ret,frame = videostream.read()
        show_image(frame)
def display_video():
    Thread(target = read_frame, args = (), daemon = True).start()

display_video()
   
while True:
    try:
        colorlist = get_frame_color(frame)
        if colorlist is not None:
            color = colorlist[0]
            if color == "Black":
                print("No color has been detected.")
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
    except:
        break                
cv2.destroyAllWindows()
videostream.release()
