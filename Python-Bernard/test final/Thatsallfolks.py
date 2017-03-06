i=''
while(True):
    if(i=='no' or i=='n'):
        print('That\'s all Folks!')
        break
    else:
        i = input("Do you want to continue? (y/n): ")
        i.lower()
