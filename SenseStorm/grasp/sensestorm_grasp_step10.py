import sys
sys.path.append('/home/pi/Desktop/sensestorm_TM2_helper')
import os
os.chdir('/home/pi/Desktop/sensestorm_TM2_helper')

''' --- Above codes in pre-processing part --- '''

from quantized_helper import load_tm2_model, classify_image, file_move
import cv2
from time import sleep
from CourseHeader.API import show_image
from sensestorm import Motor, UltrasonicSensor

def reset():
    angle = motor_move.get_angle() - angle_init
    print('angle: ',angle)
    motor_move.run_angle(0.5, angle/360)
    ultra_sensor = UltrasonicSensor("1")
    distance = ultra_sensor.get_distance()
    print('distance: ',distance)

def grab():
    global grab_flag
    if not grab_flag:
        motor_grab.run_time(50, 0.5)
        sleep(1)
        grab_flag = True

def release():
    global grab_flag
    if grab_flag:
        motor_grab.run_time(-50, 0.5)
        sleep(1)
        grab_flag = False    
        
def control_claw_state(index):
    if index == 0:
        release()
    elif index == 1:
        grab()
        
# initialize motors
motor_grab = Motor("D")
motor_move = Motor("A")
# set motor init angle
angle_init = motor_move.get_angle()
print('angle: ',angle_init)

# grab/release
global grab_flag
grab_flag = False

# select classification model and load it
input_name = 'Converted_tflite_quantized'
# move model zipped file from USB to SenseStorm
# don't need to use this function if a model exists and you don't want to replace it 
file_move(input_name)

# set up interpreter and labels from your model
interpreter, labels = load_tm2_model(input_name)
interpreter.allocate_tensors()

#create camera object
cap = cv2.VideoCapture(0)
#擷取畫面 寬度 設定為640
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
#擷取畫面 高度 設定為480
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret,image_src =cap.read()

    frame_width=image_src.shape[1]
    frame_height=image_src.shape[0]

    cut_d=int((frame_width-frame_height)/2)
    crop_img=image_src[0:frame_height,cut_d:(cut_d+frame_height)]
    image=cv2.resize(crop_img,(224,224),interpolation=cv2.INTER_AREA)

    results = classify_image(interpreter, image)
    label_id, prob = results[0]
    control_claw_state(label_id)

    print(labels[label_id],prob,label_id)
    cv2.putText(crop_img,labels[label_id] + " " + str(round(prob,3)), (5,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)

    show_image(crop_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
