from ..Program.my_robot import *

# Just testing the battery values
# and print them out
# Zeile

br = my_robot()

print("current: " + str(br.hub.battery.current()))
print("voltage: " + str(br.hub.battery.voltage()))
print("Normal fully charged voltage is around 8000")