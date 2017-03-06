##Sam Luther

def count(p):
    lows = "aeiou"
    ups =  "AEIOU"

    numberOfe = 0
    totalChars = 0
    for achar in p:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1

    percent_with_e = (numberOfe / totalChars) * 100
    print("Your text contains", totalChars, " vowels of which", numberOfe, "(", percent_with_e, "%)", "are 'e'.")

while(True):
    p = input(str('What string would you like to count: '))
    count(p)
