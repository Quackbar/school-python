import random
import string
def is_letter_in_word():
    alphie = string.ascii_letters
    i = random.randint(0,len(alphie))
    randLetter = alphie[i]
    print('The letter is '+randLetter)
    userI=''
    while(True):
        if(randLetter in userI):
            print("you guessed it!!")
            print('The letter is '+randLetter)
            break
        else:
            userI=input('Please enter a word that can contain the random letter. ')
is_letter_in_word()
