from Vex import *;
#
# Authors: 
#
# 
#--------------------------------------------   
#Authors : 
#
#Description : this program is used to control the VexRobotics robot for over undercompetition taking place on january 13 in MSOE
#
#--------------------------------------------

#--------------------------------------------
#
#wiring guide : basically relevant parts list for the code
#
#
#
#--------------------------------------------


#defining variables for the motors and sensors

#Brain
brain = Brain()

controller = Controller()

#motors - will need adjustment
left_motor1 = MOTOR(PORT1, GEAR_RATIO18, True) 
left_motor2 = MOTOR(PORT2, GEAR_RATIO18, True)
right_motor1 = MOTOR(PORT3, GEAR_RATIO18, False)
right_motor2 = MOTOR(PORT4, GEAR_RATIO18, False)
wings_motor = MOTOR(PORT5, GEAR_RATIO18, False)
claw_motor = MOTOR(PORT6, GEAR_RATIO18, False)
launcher_motor = MOTOR(PORT7, GEAR_RATIO18, False)






#
# The purpose of this method is to move the robot in a straigt line either to the front or to the back
#we need to figure out how to do implement this method
#
def goto(X_Cord,Y_Cord,Speed):
    print("going to X_Cord,Y_Cord")
    
#
# The purpose of this method is to move allow for the robot to turn it in a certain angle 
#depending on the direction of turning some wheels will be moving forward and some will be moving backwards
#    
    
def turn(turn_angle):
    print("turning")

#
# The purpose of this method is to move the robot in a straigt line either to the front or to the back
# #we need to figure out how to do implement this method
#       
def autonomous():  
    #move forward
    left_motor1.run(100)

    print("autonomous")
    
#
# The purpose of this method is to move the robot in a straigt line either to the front or to the back
# #we need to figure out how to do implement this method 
#       
def usercontrolled():
    while(True):
        if (controller.button.up.pressing()):
            left_motor1.run(100)
            left_motor2.run(100)
            right_motor1.run(100)
            right_motor2.run(100)
        elif (controller.button.down.pressing()):
            left_motor1.run(-100)
            left_motor2.run(-100)
            right_motor1.run(-100)
            right_motor2.run(-100)
        elif (controller.button.left.pressing()):
            left_motor1.run(-100)
            left_motor2.run(-100)
            right_motor1.run(100)
            right_motor2.run(100)
        elif (controller.button.right.pressing()):
            left_motor1.run(100)
            left_motor2.run(100)
            right_motor1.run(-100)
            right_motor2.run(-100)  
#
# 
# the further methods will be determined as we go along/get to know about the design of the robot itself    