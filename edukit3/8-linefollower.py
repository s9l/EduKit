# CamJam EduKit 3 - Robotics
# Worksheet 5 - Line Detection

import time
from gpizero import LineSensor

# Set variables for the GPIO pins
pinLineFollower = 25

sensor = LineSensor(pinLineFollower)

# Define the function that will be called when the line is
# detected or not detected
def lineseen():
    global isoverblack, linelost
    print("The line has been found.")
    isoverblack = True
    linelost = False
    robot.value = motorforward

def linenotseen():
    global isoverblack
    print("The line has been lost.")
    isoverblack = False

# Tell the program what to do with a line is lineseen
sensor.when_line = lineseen
# And when no line is seen
sensor.when_no_line = linenotseen

try:
    # Repeat the next indented block forever
    while True:
        time.sleep(10)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")
