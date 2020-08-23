# Camjam Edukit 3 - Robotics
# Worksheet 4 - Driving and Turning

import time # Import the Time library
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

robot.stop()


robot.forward()
time.sleep(1)

robot.backward()
time.sleep(0.5)

robot.right()
time.sleep(0.5)

robot.stop()
