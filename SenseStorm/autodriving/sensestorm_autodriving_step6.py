import time
import sys
sys.path.append('/home/pi/Desktop/objectdet/Projects/SenseStudy')
import os
os.chdir('/home/pi/Desktop/objectdet/Projects/SenseStudy')
import argparse
import cv2
import numpy as np
import pandas as pd
from sensestorm import run, speak
from threading import Thread
from CourseHeader.API import show_image
from file_transfer import file_move
from tflite_runtime.interpreter import Interpreter

previous_object = None
detected_object = None

class VideoStream:
    def __init__(self):
        self.stream = cv2.VideoCapture(0)   
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.imW = self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.imH = self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def start(self):
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        while True: 
            if self.stopped:
                self.stream.release()
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

def detect_trafficlight(frame):
    if mirror:
        frame = cv2.flip(frame,1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height))
    input_data = np.expand_dims(frame_resized, axis=0)
    if floating_model:
        input_data = (np.float32(input_data) - input_mean) / input_std
    interpreter.set_tensor(input_details[0]['index'],input_data)
    interpreter.invoke()
    boxes = interpreter.get_tensor(output_details[0]['index'])[0] 
    classes = interpreter.get_tensor(output_details[1]['index'])[0] 
    scores = interpreter.get_tensor(output_details[2]['index'])[0] 
    i = np.argmax(scores)
    object_name = 'None'
    if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
        ymin = int(max(1,(boxes[i][0] * imH)))
        xmin = int(max(1,(boxes[i][1] * imW)))
        ymax = int(min(imH,(boxes[i][2] * imH)))
        xmax = int(min(imW,(boxes[i][3] * imW)))
        cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)
        object_name = labels[int(classes[i])] 
        label = '%s: %d%%' % (object_name, int(scores[i]*100)) 
        labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) 
        label_ymin = max(ymin, labelSize[1] + 10) 
        cv2.rectangle(frame, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) 
        cv2.putText(frame, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) 
        global detected_object
        detected_object = int(classes[i])
        return frame, object_name
    else:
        return frame, 'None'

parser = argparse.ArgumentParser()
parser.add_argument('--model', help='File path of .tflite file.', required=False, default='model/detect.tflite')
parser.add_argument('--labels', help='File path of labels file.', required=False, default='model/labelmap.txt')
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects', default=0.8)
parser.add_argument("-m", "--mirror", action='store_true', default=False, help="flip camera frame")
args = parser.parse_args()
min_conf_threshold = float(args.threshold)
mirror = args.mirror
file_move()

CWD_PATH = os.getcwd()
parentPath = os.path.abspath(os.path.join(CWD_PATH, os.pardir))
path_to_model = os.path.join(CWD_PATH,'model/detect.tflite')
path_to_labels = os.path.join(CWD_PATH,'model/labelmap.txt')
with open(path_to_labels, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

interpreter = Interpreter(model_path=path_to_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]
floating_model = (input_details[0]['dtype'] == np.float32)
input_mean = 127.5
input_std = 127.5
frame_rate_calc = 1
freq = cv2.getTickFrequency()
videostream = VideoStream().start()
time.sleep(1)
imW = videostream.imW
imH = videostream.imH

while True:
    t1 = cv2.getTickCount()
    cap = videostream.read()
    frame, object_name = detect_trafficlight(cap)
    cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0))
    cv2.imshow('Object detector', frame)
    show_image(frame)
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc= 1/time1
    current_object = detected_object
    if current_object == 0 and previous_object != 0:
        #enter code for label0
        print("go") #label0 is go in the sample
        speak("go")
    if current_object == 1 and previous_object != 1:
        #enter code for label1
        print("left") #label1 is left in the sample
        speak("left")
    if current_object == 2  and previous_object != 2:
        #enter code for label2
        print("right") #label2 is right in the sample
        speak("right")
    if current_object == 3 and previous_object != 3:
        #enter code for label3
        print("stop") #label3 is stop in the sample
        speak("stop")
    if current_object == 4 and previous_object != 4:
        #enter code for label4
        print("u_turn") #label4 is uturn in the sample
        speak("u-turn")
    else:
        pass
    time.sleep(0.1)
    previous_object = current_object

    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
videostream.stop()
