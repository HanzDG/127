#Name: Hanz De Guzman
#Email: hanz.deguzman87@myhunter.cuny.edu
#Date: September 13, 2021
#This program shifts the characters by 13

a = input('Enter a word: ').upper()
b = ''
for i in a:
    if ord(i) - 13 < ord('A'):
        b += chr(ord(i) - 13 + 26)
    elif i == ' ':
        b += ' '
    else:
        b += chr(ord(i) - 13)

print("Your word in code is ",b)
    
    
