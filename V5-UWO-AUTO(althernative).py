from vex import *

# Setup and initialization of motors
brain = Brain()
drive_left = Motor(Ports.PORT1)
drive_right = Motor(Ports.PORT2)
arm = Motor(Ports.PORT3)  # Assuming this motor controls a mechanism to pick up Triballs

# Movement parameters based on the field's configurations and the robot's capabilities
# These params need to be determined through testing
motor_voltages = [
    12,  # Voltage to move to Triball
    -12, # Voltage to move to scoring zone
    # Additional voltages as needed
]
time_intervals = [
    1000,  # Time to move to Triball
    1500,  # Time to move to scoring zone
    # Additional times as needed
]

# Autonomous actions
def autonomous():
     # Assuming the robot can make 3 attempts in 15 seconds
    for _ in range(3): 
        for i, voltage in enumerate(motor_voltages):
            # set_voltage:set_voltage(): to control the motors. This is a direct method of controlling motor output, providing 
            # consistency in motor power regardless of battery level. The modification to the motor control method 
            # would be based on the need for precision. If testing showed that voltage control wasn't precise enough,
            # we might consider using speed control with feedback from encoders.
            drive_left.set_voltage(voltage)
            drive_right.set_voltage(voltage)


            # Wait for the action to complete
            wait(time_intervals[i], MSEC)

            # Stop motors after each movement
            # After each action, the motors are stopped to prepare for the next movement. 
            # This is a necessary step to prevent unwanted motion from affecting the next action 
            # and to ensure the robot has fully completed one task before starting another.
            drive_left.stop()
            drive_right.stop()

            # Handling Triball pick up and scoring
            if i == 0:  # If this is the action to reach the Triball
                arm.spin(FORWARD, 50, PERCENT)
                wait(1000, MSEC)
                arm.stop()
            elif i == 1:  # If this is the action to deposit the Triball
                arm.spin(REVERSE, 50, PERCENT)
                wait(1000, MSEC)
                arm.stop()

# Run the autonomous routine
autonomous()