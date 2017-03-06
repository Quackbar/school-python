##Sam Luther
##FindHypot: It finds the hypotenuse
##11/3/16


print('Using the equation a^2+b^2=c^2 this program will find the hypotenuse of a triangele.')
a=float(input("Input an A value:"))
b=float(input("Input an B value:"))


def findHypot(a,b):
    c = float((a**2+b**2)**.5)
    print(c)

findHypot(a,b)
