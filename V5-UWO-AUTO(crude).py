from vex import *

# Setup and initialization of motors
brain = Brain()
drive_left = Motor(Ports.PORT1)
drive_right = Motor(Ports.PORT2)
arm = Motor(Ports.PORT3)  # Assuming this motor controls a mechanism to pick up Triballs

# Autonomous actions with voltage levels and corresponding time intervals
actions = [
    {"voltage": 12, "time": 1000},  # Move forward to Triball
    {"voltage": -12, "time": 1500},  # Move backward after pickup
]

def autonomous():
    # Assuming the robot can make n attempts in 15 seconds
    for attempt in range(3):  
        for action in actions:
            
            # Apply voltage to both motors
            # set_voltage:set_voltage(): to control the motors. This is a direct method of controlling motor output, providing 
            # consistency in motor power regardless of battery level. The modification to the motor control method 
            # would be based on the need for precision. If testing showed that voltage control wasn't precise enough,
            # we might consider using speed control with feedback from encoders.
            drive_left.set_voltage(action["voltage"])
            drive_right.set_voltage(action["voltage"])

            # Wait for the action to complete
            wait(action["time"], MSEC)
            
            # Stop motors after each movement
            # After each action, the motors are stopped to prepare for the next movement. 
            # This is a necessary step to prevent unwanted motion from affecting the next action 
            # and to ensure the robot has fully completed one task before starting another.
            drive_left.stop()
            drive_right.stop()
            
            # Special action for picking up Triball
            if action is actions[0]:  # If this is the action to reach the Triball
                arm.spin(FORWARD, 50, PERCENT)  # Pick up Triball
                wait(1000, MSEC)  # Adjust based on mechanism's speed and timing
                arm.stop()
            
            # Special action for depositing Triball
            if action is actions[1]:  # If this is the action to deposit the Triball
                arm.spin(REVERSE, 50, PERCENT)  # Deposit Triball
                wait(1000, MSEC)  # Adjust based on mechanism
                arm.stop()

# Run the autonomous function
autonomous()