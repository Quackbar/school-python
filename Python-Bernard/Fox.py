# -----------------------------------------+
# Sam Luther                               |
# Fox.py                                   |
# Last Updated: October, 18, 2016          |
# -----------------------------------------|
# Use loops to minimize repeated words and |
# phrases to these lyrics of "The Fox".    |
# -----------------------------------------+

print("Dog goes woof, cat goes meow.")
print("Bird goes tweet, and mouse goes squeak.")
print("Cow goes moo. Frog goes croak, and the elephant goes toot.")
print("Ducks say quack and fish go blub, and the seal goes",end='')
for i in range(3):
    print(' Ow',end='')
print('.')
print()
print("But there's one sound that no one knows...")
print("WHAT DOES THE FOX SAY?")
print()
for i in range(3):
    if(i==0):
        start = 'Ring'
    else:
        start = 'Gering'
    print(start+" ding ding ding dingeringeding!")
    

print("WHAT THE FOX SAY?")
for i in range(3):
    print("Wa",end='')
    for i in range(5):
        print(' pa',end='')
    print(" pow!")

