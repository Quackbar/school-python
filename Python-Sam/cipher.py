
print()

def substitutionCipher(message,cipherString):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encryptedMessage = ""
    message = message.lower()
    for letter in range(len(message)):
        found = False
        for alphaLetter in range(len(alphabet)):
            if(message[letter] == alphabet[alphaLetter]):
                encryptedMessage += cipherString[alphaLetter] 
                found = True
        if found == False:
            encryptedMessage += message[letter]
    return encryptedMessage

userMessage = input('Enter a word to be encrypted:')
mappingString = input('Enter a cipher string:')
print('The encrypted message = '+substitutionCipher(userMessage,mappingString))
                
