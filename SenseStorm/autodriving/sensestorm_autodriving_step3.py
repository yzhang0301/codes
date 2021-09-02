import sys
sys.path.append('/home/pi/Desktop/sensestorm_TM2_helper')
import os
os.chdir('/home/pi/Desktop/sensestorm_TM2_helper')
from quantized_helper import load_tm2_model, classify_image, file_move
import cv2
from CourseHeader.API import *
import time
previous_id = None
input_name = 'converted_tflite_quantized'
file_move(input_name)
interpreter, labels = load_tm2_model(input_name)
interpreter.allocate_tensors()
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret,image_src =cap.read()
    if ret:
        frame_width=image_src.shape[1]
        frame_height=image_src.shape[0]
        cut_d=int((frame_width-frame_height)/2)
        crop_img=image_src[0:frame_height,cut_d:(cut_d+frame_height)]
        image=cv2.resize(crop_img,(224,224),interpolation=cv2.INTER_AREA)
        results = classify_image(interpreter, image)
        label_id, prob = results[0]
        if round(prob,3) > 0.8:
            current_id = label_id
            if current_id == 0 and previous_id !=0:
                #enter code for label0
                print("left") #label0 is left in the sample
                speak("left")
            if current_id == 1 and previous_id !=1:
                #enter code for label1
                print("stop") #label1 is stop in the sample
                speak("stop")
            if current_id == 2 and previous_id !=2:
                #enter code for label2
                print("go") #label2 is go in the sample
                speak("go")
            if current_id == 3 and previous_id !=3:
                #enter code for label3
                print("right") #label3 is right in the sample
                speak("right")
            if current_id == 4 and previous_id !=4:
                #enter code for label4
                print("u_turn") #label4 is uturn in the sample
                speak("u-turn")
            else:
                pass
            time.sleep(0.1)
            previous_id = current_id
        cv2.putText(crop_img,labels[label_id] + " " + str(round(prob,3)), (5,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        cv2.imshow('Windows',crop_img) #Raspberry pi
        show_image(crop_img) #SenseStudy
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
