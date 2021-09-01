motor_belt = Motor("A")

def convey_short():
    motor_belt.run_angle(0.5, -0.6)
    sleep(2)
    
def convey_long():
    motor_belt.run_angle(0.5, -1.2)
    sleep(3)

convey_short()
sleep(3)
convey_long()


motor_sort = Motor("B")

def left_sort():
  motor_sort.run_angle(0.5, -1.01)
  sleep(2)

def right_sort():
  motor_sort.run_angle(0.5, 1)
  sleep(2)

left_sort()
sleep(3)
right_sort()
