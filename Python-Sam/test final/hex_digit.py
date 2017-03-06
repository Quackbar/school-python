import random

hexy = '0123456789ABCDEF'
userI = ''
def is_hex_digit(hexy, userI, i):
    if(userI == hexy[i]):
        return False
    else:
        return True
#i=0
i = random.randint(0,len(hexy))
is_hex_digit(hexy, userI,i)
while(is_hex_digit(hexy, userI,i)):    
    userI = input('Try to guess a random digit from the list 0123456789ABCDEF:')
    is_hex_digit(hexy, userI,i)
if(is_hex_digit(hexy, userI,i) == False):
    print("Good Job!")    
    
    
