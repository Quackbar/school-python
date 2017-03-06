##Sam Luther
##CylinderArea
##TEST
import math
pi = math.pi


radius = float(input("Please enter the radius: "))
height = float(input("Please enter the height: "))

def cylinderArea(radius,height):
    area = (pi*radius*2*(height+radius))
    area=str(area)
    return (area)

print(cylinderArea(radius,height))

