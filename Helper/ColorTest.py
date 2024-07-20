from ..Program.my_robot import *

# This program is just for testing the values seen by the robot
# for different colors as seen by the light sensor, and what it
# is matched to by the my_robot class
br = my_robot()

while True:
    curHsv = br.colorSensor.hsv(True)
    curCol = br.colorSensor.color()
    print(str(curHsv) + "; Matches " + str(curCol))
    wait(500)