def direction_judge(target_x):
    motor_c = Motor("C")
    print("target_x ",target_x)
    if target_x and target_x < 200:
        motor_c.run_time(-35,0.01)
    elif target_x and target_x > 450:
        motor_c.run_time(35,0.01)
    sleep(0.5)
    
direction_judge(100) #Target at Left
sleep(3)
direction_judge(300) #Target at Middle
sleep(3)
direction_judge(500) #Target at Right
sleep(3)

def distance_judge(width):
    if width > 280:
       Motor("A").run_time(40,1)
    elif width > 180:
        Motor("A").run_time(60,1)
    elif width > 100:
        Motor("A").run_time(80,1)
        
distance_judge(290) #Close
sleep(2)
distance_judge(190) #Medium
sleep(2)
distance_judge(110) #Far
sleep(2)
distance_judge(10) #Too far
sleep(2)
