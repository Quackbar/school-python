##FAreaOfCircle
##Sam Luther
##10/7/16

import math
pi = math.pi

radi = input('Please input a circles radius:')
radi = float(radi)

def circlearea(radi):
    area = (pi*radi**2)
    area=str(area)
    return (area)

print(circlearea(radi))
