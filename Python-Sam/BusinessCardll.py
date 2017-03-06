#BusinessCardll
#Sam Luther
#9/13/16
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
##      /____\/____\      C(")(")\

name1 = input('Please enter your first name:')
name1l = len(name1)
lowerFirstName = name1.lower()
name2 = input('Please enter your last name:')
name2l = len(name2)
pn = input('Please enter your phone number in (XXX)-XXX-XXXX format:')

spaces = (32-(int(name1l)+int(name2l)))

space2 = ''
while(spaces!=0):
    space2 = (''+space2+' ')
    spaces = spaces - 1

spaces = (10-(int(name1l)))
space3 = ''
while(spaces!=0):
    space3 = (''+space3+' ')
    spaces = spaces - 1


print('+-------------------------------------------------+')
print('|    |                                            |')
print('|   -|          '+name2+', '+name1+ space2+'|')
print('|  --|          Tribute Liabilities Associate     |')
print('| ---|          Parasail Capital                  |')
print('| ---------                                       |')
print('|  -------      4 Hunger Plaza                    |')
print('|               STE 1400                          |')
print('|               District 12, Panem 00012          |')
print('|                                                 |')
print('| Work: '+pn+'  @: '+lowerFirstName+'@parasail.com'+space3+'|')
print('+-------------------------------------------------+')
