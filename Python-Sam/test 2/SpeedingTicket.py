##Sam Luther
##SpeedingTicket.py
##12/8/16

from random import randint
speed = 1

while(speed>0):
    speed = int(input('What was the speed over the speed limit that you were travelling: '))
    if(speed<=10 and speed>0):
        print('Your fine will be $20.')
    elif(speed<=20 and speed>=11):
        print('Your fine will be $40.')
    elif(speed<=30 and speed>=21):
        print('Your fine will be $70.')
    elif(speed<=0):
        print('Invalid Input')
    else:
        fine = 100 + randint(100,200) 
        print('Your fine will be $'+str(fine))
