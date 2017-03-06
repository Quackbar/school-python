##mySqrt
##Sam Luther
##10/10/16
##_________      ______________________
##\_____  |      |  __________________/
##    \ | |      | | /
##     \| |______| |/
##     /            \
##    |--||||-||||---|
##    |  \||/ \||/   |
##     |     oo     |
##      \___/\/\___/
##         |____|
##        /      \
##       /        \
##      /          \
##     /  |      |  \
##    |   |      |   |
##    |   |      |   |
##    /___\______/___\
##       |        |       (\ /)
##       |   __   |       (^_^)
##      /____\/____\      C(")(")

n = int(input('what number would you like to square root: '))

def mysqrt(n):
    oldguess = n/2
    for i in range(20):
        newguess = (1/2) * (oldguess + (n/oldguess))
        oldguess = newguess

    print(newguess)

mysqrt(n)
    
