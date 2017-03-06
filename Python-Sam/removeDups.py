

def remove_dups(string):
    finalString = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    alphabetNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range(len(string)):
        for i in range(len(alphabet)):
            if(alphabet[i]==string[x].lower()):
                if(alphabetNum[i]==0):
                    finalString += alphabet[i]
                    alphabetNum[i] = 1
    print(finalString)

string = input('Enter a string you would like to remove the duplicates from:')
remove_dups(string)

