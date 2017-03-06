##Sam Luther
##CylinderArea
##TEST
import math
pi = math.pi


radius = float(input("Please enter the radius: "))
height = float(input("Please enter the height: "))

def cylinderarea(radius,height):
    area = (pi*radius*2*(height+radius))
    area=str(area)
    return (area)

print(cylinderarea(radius,height))

